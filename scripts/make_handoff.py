#!/usr/bin/env python3
"""Builds docs/Chronometer_design_handoff.pdf - a self-contained design brief for an
outside reviewer. Run ./build.sh first so images/ is current."""
import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
OUT = os.path.join(ROOT, "docs", "Chronometer_design_handoff.pdf")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontSize=17, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontSize=12.5, spaceBefore=10, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle("B", parent=ss["BodyText"], fontSize=9.5, leading=13)
SM = ParagraphStyle("SM", parent=B, fontSize=8.5, leading=11)
CAP = ParagraphStyle("CAP", parent=B, fontSize=8.5, leading=11, textColor=colors.HexColor("#444444"),
                     alignment=1)
CELL = ParagraphStyle("CELL", parent=B, fontSize=8.5, leading=10.5)


def P(t, st=B):
    return Paragraph(t, st)


def bullets(items):
    return [P("&bull;&nbsp; " + t, B) for t in items]


def fig(name, caption, width=170):
    path = os.path.join(IMG, name) if not os.path.isabs(name) else name
    im = Image(path, width=width * mm, height=width * mm * 0.75 if "sheets" not in path else width * mm * 0.326)
    return KeepTogether([im, P(caption, CAP), Spacer(1, 4)])


def pair(a, ca, b, cb, w=86):
    def one(n, c):
        return [Image(os.path.join(IMG, n), width=w * mm, height=w * mm * 0.75), P(c, CAP)]
    t = Table([[one(a, ca), one(b, cb)]], colWidths=[(w + 2) * mm] * 2)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return KeepTogether([t, Spacer(1, 4)])


def table(rows, widths, header=True):
    data = [[P(c, CELL) for c in r] for r in rows]
    t = Table(data, colWidths=[w * mm for w in widths], repeatRows=1 if header else 0)
    style = [("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#999999")),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e2d0")))
    t.setStyle(TableStyle(style))
    return t


s = []
s += [P("The Chronometer &mdash; design handoff for independent review", H1),
      P("A 3D-printed mechanical puzzle instrument for a family scavenger hunt, "
        "<i>The Timekeeper's Paradox</i> (26 November 2026). Four identical units will be built on a "
        "Bambu Lab P1S (PLA/PETG, AMS) with M3 hardware.", B),
      Spacer(1, 4),
      P("<b>To the reviewer.</b> You are being asked to critique this design, not to restate it. "
        "It exists only in CAD: <b>nothing has been printed or physically tested</b>. Please look for "
        "mechanical conflicts, features that will not print or will not survive handling, tolerance "
        "choices that are wrong for FDM PLA, and simpler alternatives. Specific questions are listed "
        "in section 8. A first review round has already been applied (running-fit bayonet with a sprung latch, "
        "contacting fragment clamp, captive nut, more ring play). Dimensions are millimetres. The renders are flat-colour OpenSCAD previews of the "
        "real geometry; surface decoration has deliberately not been added yet.", B)]

s += [P("1. What the finished instrument looks like", H2),
      fig("fn0_as_issued.png",
          "As handed to players: knurled outer hour ring (dark), fixed brass index ring with a double arrow at XII "
          "and three M3 screws, inner symbol ring (ivory, 12 label pockets), centre cover with eight peg sockets "
          "and the keystone knob.", 150),
      table([["Overall", "Ø125 mm; 19.6 mm thick at the rim; 29.6 mm over the centre knob"],
             ["Printed parts per unit", "18 (base, deck, 2 rings, index cap, 4 detent pawls, cover, keystone, "
                                        "UV retaining ring / latch spring, mask, door, 4 fragments)"],
             ["Hardware per unit", "3 × M3×16 socket-head screws (self-tapped into 2.8 mm pilots), "
                                   "1 × M3×8 screw, 1 × M3 nut"],
             ["Printing", "All parts support-free, 0.2 mm layers, 0.4 mm nozzle. No glue on moving parts."],
             ["Flashlight", "Flat squeeze-type coin-cell key-fob UV light, about 43.5 × 23 × 8.5 mm "
                            "(scaled from photos, ±1 mm)"]],
            [38, 138], header=False)]

s += [PageBreak(), P("2. How it functions", H2),
      P("The instrument has four functions that players discover in sequence.", B),
      P("<b>Function 1 &mdash; Temporal Alignment.</b> Two concentric rings rotate independently, each with "
        "12 detented positions. The outer ring is the rim of the instrument and is turned by its knurled edge; "
        "the inner ring is turned by raised finger ribs. Both are read against the fixed double arrow at XII. "
        "The outer ring carries Roman numerals; the inner ring has 12 shallow pockets for replaceable symbol "
        "stickers. Decoding of an alignment is done with an external chart.", B),
      P("<b>Function 2 &mdash; Temporal Aperture.</b> The centre cover is a three-lug bayonet with a sprung "
        "latch: 28° anticlockwise and lift. That exposes a 50 mm well with an opaque stencil at the bottom, 0.8 mm above the paper, with "
        "four Ø10.5 mm apertures and a centre sighting hole. The instrument is placed on a printed clue sheet, "
        "four notches in the base rim are lined up with printed ticks (double notch = top), and the apertures "
        "isolate four letters.", B),
      pair("fn1_top.png", "Function 1: top view. Rings read against the arrow at XII.",
           "fn2_aperture.png", "Function 2: cover removed, stencil at the bottom of the well."),
      Image(os.path.join(ROOT, "sheets", "aperture_proof.png"), width=176 * mm, height=176 * mm * 0.326),
      P("Simulated view of the test sheet: bare sheet, mask registered (reads T-I-M-E clockwise from top), and mask "
        "misplaced by 1 mm in x and y.", CAP),
      PageBreak(),
      P("<b>Function 3 &mdash; Hidden UV Discovery.</b> The flashlight lies flat in a bay inside the base, "
        "41.5 mm off-centre so it is clear of the well. It is closed by a flush 2 mm dovetail door in the back "
        "face that slides out through the rim and is held by a side spring clicking into a notch. The back of "
        "the instrument stays flat so it still sits on the clue sheet. The UV-reactive paper insert is a Ø46 mm "
        "disc inside the centre cover, held by a printed split ring.", B),
      P("<b>Function 4 &mdash; Final Synchronization.</b> Four fragments collected during the hunt dock onto "
        "the face of the centre cover. Each has two pegs at radii unique to its socket, so it fits one position "
        "one way up. The keystone knob (M3 thumbscrew into a captive nut) clamps all four: its cone seats on "
        "their 45° bevels with 0.3 mm left under the knob. "
        "Together they form a ring of 12 characters directly inside the inner dial. The final clue first names one setting symbol "
        "to bring to the index arrow (it is not read), then four symbols to read in order; each points at one "
        "character. Demo: set the sun to the index, then read moon, star, hourglass, diamond = <b>1847</b>; one "
        "click off gives 5020.", B),
      pair("fn3_uv.png", "Function 3: back view, door slid out, flashlight (purple stand-in) removed from its bay.",
           "fn4_final.png", "Function 4: four fragments seated and clamped by the keystone.")]

s += [P("3. Construction", H2),
      pair("section.png", "Section through the centre. Right: flashlight bay and door. Centre: cover, well, mask.",
           "exploded.png", "Exploded view."),
      Image(os.path.join(IMG, "clamp_section.png"), width=150 * mm, height=150 * mm * 760 / 1500),
      P("Fragment clamp, true section with the keystone tightened.", CAP),
      table([["Part", "Role", "Key features"],
             ["Base (12 mm)", "Rear module", "Flat back; mask ledge and keyway; 4 rim notches for sheet "
                                             "registration; flashlight bay open to the deck above; dovetail door slot"],
             ["Deck (5 mm)", "Ring mechanism", "2 mm floor; hub (R25&ndash;28) and fixed rib (R42&ndash;48) are "
                                               "the ring journals; 4 pawl pockets in the rib; bayonet seat in the well wall"],
             ["Outer ring", "Hours", "L-section, R48.3&ndash;62.5, 5.6 mm tall; 12 scallops on its inner journal face; knurled rim"],
             ["Inner ring", "Symbols", "L-section, R28.3&ndash;41.65; 12 scallops on its outer flange; label pockets; finger ribs"],
             ["Index cap", "Retainer + index", "Flat ring R40&ndash;50 × 2.4 mm screwed to the rib; overlaps both ring "
                                               "flanges by 1.7 mm and closes the pawl pockets"],
             ["Pawls ×4", "Detents", "Arc leaf springs, 36° long, 1.2 × 2.7 mm section, supported on two feet, "
                                     "rounded nose at mid-span"],
             ["Centre cover", "Lid + fragment carrier", "Ø55.6 flange standing 3 mm proud, knurled; skirt with 3 bayonet "
                                                        "lugs at unequal spacing; nut pocket; 8 keyed peg sockets"],
             ["Mask", "Stencil", "1.2 mm disc; key tab; 3 in-plane spring arms with nubs that click into a groove in the well wall"],
             ["Door", "UV compartment lid", "2 mm plate with 45° dovetail edges; in-plane cantilever side spring with a detent nub"],
             ["Fragments ×4", "Code carriers", "2.4 mm quarter-ring tiles, 2 pegs each, 3 debossed characters, 45° inner bevel"],
             ["Keystone", "Fragment clamp", "Ø20 knurled knob with conical underside, carries the M3×8 screw"]],
            [28, 30, 118])]

s += [P("4. Mechanism details and numbers", H2)]
s += bullets([
    "<b>Assembly stack.</b> The same three M3 screws pass through the index cap and the deck and self-tap into "
    "the base. Removing the centre cover does not touch the rings, which are trapped only by the index cap.",
    "<b>Ring fits.</b> 0.30 mm radial journal clearance; 0.35 mm axial play under the cap.",
    "<b>Detents.</b> Two pawls per ring, diametrically opposite, housed in the fixed rib. Scallops are 0.6 mm deep "
    "(R2.0); nose tip radius 1.5; 0.15 mm preload when seated; 0.75 mm deflection between positions. Estimated "
    "(not measured): ~1.8 N per pawl at peak, ~0.7 % peak bending strain, about 2&ndash;3 N at the rim to turn the "
    "outer ring. Pawls bend in the layer plane. Three stiffnesses (1.0 / 1.2 / 1.4 mm) are provided.",
    "<b>Cover bayonet.</b> Lugs project 1.4 mm with a 45° upper face; the mating ceiling in the deck is also 45° "
    "(support-free), with 0.45 mm axial play at entry easing to 0.30 mm at the hard stop: a running fit. "
    "Retention is a separate latch: the free end of the UV retaining ring (1.6 × 2.4 mm section, ~13 mm free "
    "length, bending in the layer plane) carries a nub that passes through a slot in the skirt and clicks into a "
    "0.7 mm groove in the well wall at the locked position, with a second groove at the insert position.",
    "<b>Mask.</b> 0.30 mm radial clearance; spring nubs have 0.35 mm interference with the wall and a 0.25 mm "
    "click groove. Removed by pushing up from the back. It passes down the well through one of the bayonet entry grooves.",
    "<b>Door.</b> 0.20 mm per-side clearance; nub 0.7 mm on a 2.0 × 14 mm cantilever; 0.5 mm clearance to a bridged "
    "ceiling. The bay leaves 1.5 mm total clearance on the flashlight's faces because its switch is the squeeze face.",
    "<b>Thin sections.</b> Wall between the door slot and the rim, and between the bay and the rim: 2.3&ndash;3 mm. "
    "Rib wall between pawl pocket and ring: 1.2 mm. Hub wall behind the bayonet entry grooves: 1.4 mm.",
    "<b>Print orientation.</b> Base, deck, rings, cap, mask, door, pawls: as assembled, flat side down. Cover, "
    "keystone and fragments: upside-down (visible face on the plate).",
])

s += [P("5. Departures from the original brief", H2)]
s += bullets([
    "The UV compartment is not a rear extension: a local bump would stop the instrument lying flat on the clue "
    "sheet, and a compartment behind the centre would block the aperture. It is inside a full-footprint base instead.",
    "The stencil is at the bottom of the well, not directly under the cover, to remove parallax.",
    "The body is split into deck + base so the ring mechanism can be test-printed and kept while the base is revised.",
    "The outer ring is exposed at the rim rather than enclosed by a bezel, for grip.",
    "Fragments dock on the removable centre cover rather than in the main body or on a separate accessory ring, "
    "because seats in the body would have reduced the dials to about 7 mm bands.",
    "The stencil is an interchangeable part.",
])

s += [P("6. What has been verified, and what has not", H2)]
s += bullets([
    "<b>Verified in CAD:</b> boolean intersection of every neighbouring part pair in assembled position shows zero "
    "overlapping volume, including the full swept turning path of the cover (17 checks); a fragment in the "
    "wrong socket collides; the pawl noses, mask spring nubs and cover latch engage by their intended preload; "
    "and the keystone cone reaches the fragments before its underside reaches the cover.",
    "<b>Verified geometrically:</b> the test sheet shows exactly T, I, M, E through the mask and stays clean "
    "(whole letter visible, no neighbour intruding) for placement errors up to 1.4 mm.",
    "<b>Not verified:</b> anything physical. No part has been sliced or printed. Spring forces and strains are "
    "hand calculations with E = 3 GPa. The flashlight dimensions come from photos, not calipers.",
])

s += [P("7. Risks the designer already expects", H2)]
s += bullets([
    "Cover latch force (estimated 1&ndash;2 N at the nub) and click are untested.",
    "The nut is held by a 0.35 mm undersized pocket mouth; too tight or too loose is possible.",
    "Detent feel and PLA creep if a ring is left between positions.",
    "Mask spring-arm retention is untested.",
    "The 29 mm bridged ceiling over the door could sag and rub.",
    "The deck-to-base seam has no screw across the 120° arc that spans the flashlight bay.",
    "Self-tapped M3 threads in PLA tolerate only a few assembly cycles.",
    "6.5 mm fragment characters and reading down a 22 mm deep well in poor light.",
])

s += [P("8. Questions for the reviewer", H2)]
s += bullets([
    "Is trapping both rings with a single flat cap on one flange each sufficient, or will the rings tilt or bind?",
    "Are 0.30 mm radial and 0.20 mm axial clearances right for PLA on a P1S at this diameter?",
    "Is using the UV retaining ring as the cover's latch spring sound, or does the dual role cause a problem?",
    "Are the pawl proportions sensible for PLA, and would you change the material or geometry?",
    "Is the 2 mm dovetail door with a side spring robust, and is the thin rim wall next to it a problem?",
    "Is there a simpler way to retain the mask that is still tool-free and swappable?",
    "Does clamping the fragments by a bevel under a thumbscrew over-complicate it compared with a press fit?",
    "Does the code-reading scheme (symbols on the inner ring pointing at fragment characters) have a usability flaw?",
    "Anything that will not print support-free as described, or any assembly step that cannot be done in the order implied?",
    "With two weeks to the event and four units to build, what would you cut or simplify first?",
])

s += [P("9. Source", H2),
      P("The complete parametric model is one OpenSCAD file, <font face='Courier'>cad/chronometer.scad</font> "
        "(about 600 lines); attach it alongside this document if the reviewer should check geometry directly. "
        "All dimensions quoted here are parameters at the top of that file.", B)]


def footer(canvas, doc):
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillGray(0.4)
    canvas.drawString(18 * mm, 10 * mm, "The Chronometer - design handoff for review - CAD only, not yet printed")
    canvas.drawRightString(letter[0] - 18 * mm, 10 * mm, "page %d" % doc.page)


SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm,
                  bottomMargin=17 * mm, title="The Chronometer - design handoff for review").build(
    s, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "kB")
