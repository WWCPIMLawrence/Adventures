#!/usr/bin/env python3
"""Builds docs/Chronometer_status_handoff_2026-11-16.pdf - current project status for the outside reviewer."""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from PIL import Image as PI

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "Chronometer_status_handoff_2026-11-16.pdf")
ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontSize=17, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontSize=12.5, spaceBefore=10, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle("B", parent=ss["BodyText"], fontSize=9.5, leading=13)
CAP = ParagraphStyle("CAP", parent=B, fontSize=8.5, textColor=colors.HexColor("#444444"), alignment=1)
CELL = ParagraphStyle("CELL", parent=B, fontSize=8.5, leading=10.5)
P = lambda t, st=B: Paragraph(t, st)
bullets = lambda items: [P("&bull;&nbsp; " + t) for t in items]


def table(rows, widths):
    t = Table([[P(c, CELL) for c in r] for r in rows], colWidths=[w * mm for w in widths], repeatRows=1)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#999999")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                           ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e2d0"))]))
    return t


def img(name, w_mm):
    path = os.path.join(ROOT, "images", name); w, h = PI.open(path).size
    return Image(path, width=w_mm * mm, height=w_mm * mm * h / w)


s = [P("The Chronometer &mdash; project status, 16 November 2026", H1),
     P("Four identical instruments are needed for the 26 November 2026 hunt (10 days). Bambu P1S with AMS, PLA and PETG, M3 hardware, "
       "parametric OpenSCAD. This is a status for review; the production batch has <b>not</b> been started and will not be until the fit "
       "tests pass. The owner physically tests every printed part; <b>nothing below is called passed unless the owner has reported it.</b>", B),
     Spacer(1, 4), img("parts_guide.png", 150), P("The twelve parts of one instrument, by name.", CAP)]

s += [P("1. Where we are in one paragraph", H2),
      P("The mechanical core is proven by physical test: mask, nut pocket, cover fit, both rings and their detents, flashlight bay, raised "
        "numerals and symbols, and the two-part fragment tiles. The open work is the centre cover's retention. The three-arm latch "
        "was too weak (the cover comes off when the knob is loosened) and its ring falls out. Last night's gate prototype "
        "<b>worked flawlessly in the owner's hands</b>. Two follow-ups remain before it can be adopted: the knob test, and a fix for "
        "the gate springs falling out of their seat (fixed in CAD, not yet printed). Separately, the owner's mask problem is "
        "explained by the old base, and the new base is not yet printed.", B)]

s += [P("2. Status by subsystem", H2),
      table([["Subsystem", "Status", "Evidence"],
             ["Mask / stencil, nut pocket, cover fit, rings, detents, flashlight bay", "<b>Confirmed</b>", "Owner tests, earlier sessions"],
             ["Raised numerals and symbols, fragment tiles (black inlay), ivory ribs", "<b>Confirmed</b>", "Owner: &quot;the tiles look perfect&quot;"],
             ["Brass index cap with ivory arrow; back plate with revised boss clearance", "Built, not yet printed in brass", "CAD checks only"],
             ["Mask retention (lip in the base)", "<b>Not yet tested.</b> The owner's base is the old one; it has no lip, so the mask slides and pops up. The new base and plate are not printed yet.", "Owner report today; CAD lip checked"],
             ["Three-arm latch (current production)", "<b>Failing:</b> weakens after a few openings; the cover can be knob-twisted off; its ring snags on insertion and falls out", "Owner reports"],
             ["Push-and-turn gate (variant)", "<b>Mechanism works</b> as designed (press, twist, lock; pulling does nothing). <b>Knob test pending.</b> Strips fell out of the seat, one lost", "Owner test, 16 Nov evening"],
             ["Plain ring with positive ledge (variant)", "<b>Works</b>: stays in, no snagging, no spikes", "Owner test, 16 Nov evening"],
             ["Smooth cover rim (variant)", "Printed as part of the gate cover; no feedback yet on grip or look", "&mdash;"],
             ["Knob screw head pocket (Phillips)", "<b>Held</b> until the owner supplies the screw's head size", "Awaiting measurements"],
             ["Final RIFT game sheet", "Prepared on the ChatGPT side; not yet seen here", "Awaiting file"]],
            [58, 74, 38])]

s += [P("3. The centre cover: what was learned", H2)]
s += bullets([
    "<b>Root cause of the knob problem:</b> the cover is the only part that reacts the knob's torque, and loosening turns the same way as "
    "the cover's unlocking. The old latch holds roughly 75 N&middot;mm (estimate) against a hand-tight knob of perhaps 100&ndash;300 N&middot;mm "
    "(also an estimate). Stiffer arms cannot fix it, and PETG arms creep.",
    "<b>Reversing the lock direction was rejected:</b> it only moves the problem (tightening then pushes toward release). The bayonet "
    "direction, lugs and 28&deg; travel are unchanged, as ChatGPT asked.",
    "<b>The gate:</b> a pocket at the locked end of each track, 0.9 mm deeper, ending in a vertical wall. Six printed bow springs in "
    "the hub lift the cover about 1.2 mm so the lugs rise into the pockets; the wall then blocks the unlocking turn. To open, press "
    "about 1 mm (an estimated 8&ndash;14 N) and turn. The owner confirms this works. The track diagram and the exploded view are in the gate handoff.",
    "<b>Ring:</b> the old 45&deg; bump was a ramp; the new ledge has a flat catch face. The owner finds the plain ring with the ledge "
    "stays in and does not snag.",
    "<b>Latch simplification:</b> with the gate working, the three-arm latch can go entirely (no nubs, no cover slots, no deck "
    "grooves). It also frees the hub space the springs use. <b>Recommended</b>, subject to the knob test."])
s += [Spacer(1, 3), img("gate_view.png", 105), P("Gate seat with six bow springs (red) and the cover lifted above it.", CAP)]

s += [P("4. Open problems and what is being done", H2),
      table([["Problem", "Cause", "Action / status"],
             ["Gate strips fall out of the seat when the cover is off; one lost; the soft and firm sets are mixed up",
              "Feet only 1.0 mm deep in slots with 0.15 mm clearance", "Fixed in CAD: 1.6 mm feet, 0.07 mm clearance per side. <b>Seat and both strip sets need reprinting.</b> Keep the sets apart by colour"],
             ["Mask slides and pops up", "Old base has no lip", "New base (lip) and plate already designed. <b>Print base and plate</b> (about 1.5 h and 1 h on the P1S)"],
             ["Mask may fall out when the plate is removed at the end", "With the plate off, the lip no longer holds it", "Test where it ends up. Options: take it out first, or add a small plate catch. Not designed yet"],
             ["Hidden Allen key in the base", "Would need its own hidden, order-proof door", "Recommended against; the key becomes a game object (in a clue container or handed over at the end)"]],
            [52, 50, 68])]

s += [P("5. What is unchanged", H2)]
s += bullets([
    "The approved puzzle configuration: dial prototype TIME, fragments 281 / 361 / 924 / 507, the 12-character code ring, symbols, RIFT "
    "stencil geometry (four &Oslash;10.5 holes plus a centre sighting hole), decoys 6 and 9, the UV message &quot;THE SUN IS FALSE. "
    "TRUST THE ARROW.&quot; and the flashlight as a genuine hidden surprise.",
    "Production CAD defaults. All gate, ring, latch and rim changes are optional parameters, off by default. All 30 default part "
    "exports are identical in volume and size to before, and the 27 interference checks pass. In the gate variant, the base, plate, mask, "
    "rings, index cap, keystone and fragments are also identical, and 21 gate and stack checks pass.",
    "The captive M3 nut pocket and the stencil geometry were not touched."])

s += [P("6. Proposed path to the 26th (for review)", H2),
      table([["When", "What"],
             ["Tonight / tomorrow", "Owner: knob test (0 and 4 fragments, with and without pressing down). Print the new base and plate. Reprint the seat and both strip sets"],
             ["17&ndash;18 Nov", "Decide: gate-only (no latch) or fall back to the three-arm latch. Check mask retention on the new base. Choose soft or firm strips"],
             ["~19 Nov", "<b>Freeze.</b> Master zip of final files. Parts that change from today's production set if the gate is adopted: deck, cover, ring, plus six strips per unit"],
             ["20&ndash;24 Nov", "Print the three remaining instruments plus spares (strips especially). Assemble and shake-test each"],
             ["25 Nov", "Final check of all four against the game sheet. Buffer"]],
            [30, 140])]

s += [P("7. Decisions and questions for ChatGPT", H2)]
s += bullets([
    "Adopt the gate-only variant (no three-arm latch) if the knob test passes? What would make you want the latch kept?",
    "Is a roughly 8&ndash;14 N press over 1 mm acceptable for children and weak hands? Is a locked cover standing 1.2 mm proud acceptable?",
    "Press-on-knob risk: pushing down on the knob while unscrewing would lower the cover and release it. Is that an acceptable residual risk?",
    "Mask at the end of the game: should the sequence take the stencil out first, or should the back plate carry it?",
    "Agree that the Allen key becomes a game object (in a clue container or handed over by the host) and stays out of the device?",
    "The story clue for the cover: &quot;press the dial in and turn it back.&quot; Does the time-reversal theme cover it?",
    "Please send the final RIFT sheet. The owner will send the Phillips screw's head measurements when available."])

SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
                  title="Chronometer - project status, 16 Nov 2026").build(s)
print("ok", OUT)
