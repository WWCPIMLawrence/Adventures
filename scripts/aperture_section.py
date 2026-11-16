#!/usr/bin/env python3
"""Half cross-sections (r vs height above the sheet) of the current mask arrangement and the proposed integral floor."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
BR, BK, SH, GR = "#c9a24a", "#2b2d33", "#d9d9d9", "#9aa0a6"
fig, axs = plt.subplots(1, 2, figsize=(12, 4.6), sharey=True)
def common(ax, title):
    ax.set_xlim(0, 32); ax.set_ylim(-1.2, 4.2); ax.set_title(title, fontsize=10)
    ax.add_patch(Rectangle((0, -1.0), 32, 1.0, fc=SH, ec="none")); ax.text(1, -0.6, "RIFT sheet (z = 0 is its top face)", fontsize=8)
    ax.set_xlabel("radius from the centre (mm)"); ax.grid(alpha=.2)
def box(ax, x0, x1, z0, z1, fc, lab=None, tx=None, tz=None, col="k"):
    ax.add_patch(Rectangle((x0, z0), x1 - x0, z1 - z0, fc=fc, ec="k", lw=.8))
    if lab: ax.text(tx if tx is not None else (x0 + x1) / 2, tz if tz is not None else (z0 + z1) / 2, lab, ha="center", va="center", fontsize=7.5, color=col)
# --- current ---
ax = axs[0]; common(ax, "NOW: separate mask on a ledge in the plate (base lip above)")
box(ax, 22, 32, 0, 0.6, BR, "plate ledge", 27, 0.3); box(ax, 25, 32, 0.6, 2.0, BR, "plate wall\n(click groove)", 28.5, 1.3)
box(ax, 0, 24.7, 0.6, 1.8, BK, "mask 1.2 mm (separate part, holes at r 15 +/- 5.25)", 11, 1.2, "w")
box(ax, 22, 25.1, 2.0, 3.4, GR, "base lip", 23.5, 2.7); box(ax, 25.1, 32, 2.0, 4.2, GR, "base", 28.5, 3.1)
ax.annotate("", xy=(5, 0.6), xytext=(5, 0)); ax.text(6, 0.25, "0.6 mm air gap to sheet", fontsize=7.5)
ax.text(1, 3.2, "mask top at 1.8 mm\nmask holds only by 3 spring nubs\nand the sandwich: plate ledge below,\nbase lip above", fontsize=7.5)
# --- proposed ---
ax = axs[1]; common(ax, "PROPOSED: floor printed with the plate, back face on the bed")
box(ax, 0, 25, 0, 1.2, BK, "integral floor 1.2 mm (black, 4 holes + sighting hole)\nflat on the bed, no gap to the sheet", 12.5, 0.6, "w")
box(ax, 25, 32, 0, 2.0, BR, "plate wall", 28.5, 1.0); box(ax, 25.1, 32, 2.0, 4.2, GR, "base (no lip)", 28.5, 3.1)
ax.text(1, 3.2, "no separate mask: nothing to retain\nfloor top at 1.2 mm (0.6 mm lower than now)\nplate is the only part that comes off", fontsize=7.5)
ax.text(1, 1.7, "colour change: floor layers 1-6 black,\nthe rest brass (AMS, separate body)", fontsize=7.5)
axs[0].set_ylabel("height above the sheet (mm)")
plt.tight_layout(); plt.savefig("images/aperture_section.png", dpi=170); print("ok")
