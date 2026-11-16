#!/usr/bin/env python3
"""Unrolled bayonet track with the gate: ceiling profile and the lug in its states (nominal dimensions)."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
play_end, play_free, g, slack, travel, lug_w, lift = 0.5, 0.75, 0.9, 1.0, 28.0, 10.0, 1.2
a_open, a_dwell, a_stop = -lug_w/2, -travel + lug_w/2, -travel - lug_w/2 - 0.3
top = 3.2
pts = [(8, top), (a_open, top)]
n = 6
for i in range(n - 1, -1, -1):                       # from the entry end toward the pocket
    x_hi = a_dwell + (a_open - a_dwell) * (i + 1) / n; x_lo = a_dwell + (a_open - a_dwell) * i / n
    p = play_end + (play_free - play_end) * (i + 1) / n
    pts += [(x_hi if i < n - 1 else a_open, p), (x_lo, p)]
pts += [(a_dwell + slack, play_end + (play_free - play_end) / n), (a_dwell + slack, play_end + g), (a_stop, play_end + g), (a_stop, top)]
fig, ax = plt.subplots(figsize=(11, 4.8))
poly = [(8, top + .3)] + pts + [(a_stop - 3, top), (a_stop - 3, top + .3)]
ax.fill([p[0] for p in poly], [p[1] for p in poly], color="#c9c2b3", zorder=1)
ax.plot([p[0] for p in pts[1:-1]], [p[1] for p in pts[1:-1]], color="#5a4b2b", lw=2, zorder=2)
ax.axhline(0, color="#444", lw=1.2)
def lug(xc, z, fc, label="", ls="-"):
    ax.add_patch(Rectangle((xc - lug_w/2, z - 0.5), lug_w, 0.5, fc=fc, ec="k", lw=1, ls=ls, alpha=.95, zorder=3))
    if label: ax.text(xc, z - 0.25, label, ha="center", va="center", fontsize=8.5, zorder=4)
lug(0, lift, "#e8c15a", "dropped in at the\nentry: spring lifts it")
lug(-travel, lift, "#e8c15a", "LOCKED: sprung up\ninto the pocket")
lug(-travel, 0.0, "#9bc4a0", "pressed down", "--")
lug(0, 0.0, "#9bc4a0", "pressed down", "--")
ax.annotate("", xy=(-travel, 0.1), xytext=(-travel, lift - .55), arrowprops=dict(arrowstyle="->", lw=2.2, color="#b03a2e"))
ax.text(-36.2, 0.62, "to unlock:\nPRESS\n(~9 N, 1 mm)", color="#b03a2e", fontsize=9, va="center", ha="center")
ax.annotate("", xy=(-5, -0.42), xytext=(-23.5, -0.42), arrowprops=dict(arrowstyle="->", lw=2, color="#2e7d32"))
ax.text(-14.5, -0.78, "then TURN anticlockwise while pressed (the cover goes back to the entry, to the left)", color="#2e7d32", fontsize=9, ha="center")
ax.annotate("pocket wall: stops the unlocking turn\nwhile the cover is up.\nKnob loosening lands here", xy=(a_dwell + slack, 1.2), xytext=(-12, 2.35),
            arrowprops=dict(arrowstyle="->", lw=1.3), fontsize=9, ha="center")
ax.annotate("hard stop (locking turn)", xy=(a_stop, 2.0), xytext=(-37.5, 2.7), arrowprops=dict(arrowstyle="->", lw=1.3), fontsize=9, ha="center")
ax.text(5.5, 2.4, "entry groove\n(full height)", fontsize=9, ha="center")
ax.text(-16, 0.93, "track ceiling 0.5 - 0.75 mm", fontsize=8, color="#5a4b2b", ha="center")
ax.text(7.7, 0.08, "hub top", ha="left", va="bottom", fontsize=8)
ax.set_xlim(8, -41); ax.set_ylim(-1.0, 3.5)
ax.set_xlabel("angle along the bayonet track (deg). 0 = lift-out position; the cover locks by turning clockwise, to the right")
ax.set_ylabel("height of the lug's top above\nits pressed-home position (mm)")
ax.set_title("Push-and-turn gate - unrolled track at the lugs' radius, nominal dimensions (before print droop)", fontsize=10)
ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]); ax.grid(alpha=.25)
plt.tight_layout(); plt.savefig("images/gate_track.png", dpi=170)
