#!/usr/bin/env python3
"""Builds docs/Chronometer_status_handoff.pdf - where the project stands, for an outside reviewer."""
import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
OUT = os.path.join(ROOT, "docs", "Chronometer_status_handoff.pdf")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontSize=17, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontSize=12.5, spaceBefore=10, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle("B", parent=ss["BodyText"], fontSize=9.5, leading=13)
CAP = ParagraphStyle("CAP", parent=B, fontSize=8.5, leading=11, textColor=colors.HexColor("#444444"), alignment=1)
CELL = ParagraphStyle("CELL", parent=B, fontSize=8.5, leading=10.5)


def P(t, st=B):
    return Paragraph(t, st)


def bullets(items):
    return [P("&bull;&nbsp; " + t) for t in items]


def table(rows, widths, header=True):
    t = Table([[P(c, CELL) for c in r] for r in rows], colWidths=[w * mm for w in widths], repeatRows=1 if header else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#999999")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    if header:
        st.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e2d0")))
    t.setStyle(TableStyle(st))
    return t


def pair(a, ca, b, cb, w=86):
    def one(n, c):
        return [Image(os.path.join(IMG, n), width=w * mm, height=w * mm * 0.75), P(c, CAP)]
    t = Table([[one(a, ca), one(b, cb)]], colWidths=[(w + 2) * mm] * 2)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return t


s = [P("The Chronometer &mdash; project status handoff", H1),
     P("A 3D-printed mechanical puzzle instrument for a family scavenger hunt on 26 November 2026. Four identical "
       "units, Bambu Lab P1S with AMS, PLA/PETG, M3 hardware. This document describes where the project stands "
       "at the start of physical prototyping.", B),
     Spacer(1, 4),
     P("<b>To the reviewer.</b> Please check the plan, not just the design: is the test order right, are the "
       "print settings sensible, is the schedule realistic, and what is most likely to go wrong. Questions are in "
       "section 9. All dimensions are millimetres.", B),

     P("1. Status in one paragraph", H2),
     P("The design is complete in CAD (one parametric OpenSCAD file) and has been through one outside review, whose "
       "six points have been applied. Twenty-two automated geometry checks pass. <b>Nothing has been printed, "
       "sliced in Bambu Studio, or physically tested.</b> The owner is about to print the first fit tests, is "
       "checking existing filament and hardware before buying anything, and will supply caliper measurements of "
       "the UV flashlight; the flashlight compartment is on hold until then. No full instrument and no batch of "
       "four will be printed until the fit tests pass.", B),
     Spacer(1, 4),
     pair("fn0_as_issued.png", "As issued to players (flat-colour CAD preview, no decoration yet).",
          "exploded.png", "Exploded view: 18 printed parts, 4 screws, 1 nut."),

     P("2. The instrument, briefly", H2)]
s += bullets([
    "<b>Size:</b> Ø125 mm, 19.6 mm thick at the rim, 29.6 mm over the centre knob.",
    "<b>Two dials:</b> an outer hour ring (the knurled rim) and an inner symbol ring, each with 12 detented positions, "
    "read against a fixed arrow at XII. Both are trapped by one fixed index ring held by three screws.",
    "<b>Detents:</b> four separate arc-shaped leaf springs in pockets of a fixed rib, two per ring.",
    "<b>Centre cover:</b> three-lug twist-lock, 28° turn, loose running fit. A sprung nub on the UV retaining ring "
    "inside the cover clicks into a groove in the well wall to hold it shut.",
    "<b>Aperture:</b> with the cover off, an interchangeable stencil sits at the bottom of a 50 mm well, 0.8 mm above "
    "the paper; four Ø10.5 apertures read T-I-M-E on the test sheet (clean for placement errors up to 1.4 mm).",
    "<b>UV:</b> a flat squeeze-type key-fob light lies in a bay in the base behind a flush sliding door in the back "
    "face. The UV-reactive paper disc lives inside the centre cover.",
    "<b>Final code:</b> four keyed fragments dock on the cover face and are clamped by a centre thumb-knob. They form "
    "a 12-character ring; one symbol is brought to the arrow to set the inner dial, then four named symbols each "
    "point at one character (demo: 1847).",
])

s += [P("3. What changed after the first review", H2)]
s += [table([["Review point", "Change made", "Still to be proven physically"],
             ["Fragment clamp did not touch the tiles", "Knob cone now matches the fragment bevel and seats with 0.3 mm left under the knob; nut pocket has a 0.35 mm undersized mouth", "Tiles immovable when shaken; nut stays in when the UV disc is changed"],
             ["Cover relied on a zero-clearance friction ramp", "Running fit: 0.45 mm axial play at entry, 0.30 mm locked, hard stop. Separate sprung latch (1.6 × 2.4 mm section, ~13 mm free length, 0.7 mm groove), grooves at locked and insert positions", "Insertion, full turn, removal, latch force and click, retention in transit"],
             ["Check covered end positions only", "Check now intersects the cover's full swept turning path with deck and base", "&mdash;"],
             ["UV compartment is the least essential mechanism", "Separate bay-and-door test piece; one parameter removes bay and door entirely", "Bridge sag, door slide, side-spring life, light fit"],
             ["Ring axial play too tight", "0.20 &rarr; 0.35 mm under the cap (radial stays 0.30)", "Free rotation with screws tight; rocking or tilt"],
             ["Springs unproven; mask check used a plain disc", "Check now uses the real mask (only its spring nubs may touch the wall); drop-in mask fallback; pawls in three thicknesses, PLA and PETG plates", "Click feel and settling over repeated cycles; mask arm durability"],
             ["Five symbols for four digits was ambiguous", "Decoding card separates SET (sun, double-bordered label) from READ (four numbered symbols); characters enlarged to 6.5 mm", "Readability by a first-time player in indoor light"]],
            [42, 80, 54])]

s += [P("4. First test prints (about to start)", H2),
      P("Any ordinary PLA on hand (not silk, wood-filled or glow) and any PETG. Final colours are not needed for "
        "this round. Weights and times are from PrusaSlicer with a generic machine profile, not Bambu Studio.", B),
      Spacer(1, 3),
      table([["#", "Parts on the plate", "Filament", "Weight", "Time", "Tests"],
             ["1", "Seat test piece (centre of deck + base in one, Ø66 × 9), cover, mask", "PLA", "22 g", "~2 h 20", "Twist-lock through its full turn, latch grooves, mask retention"],
             ["2", "Spring plate: 2 outer + 2 inner pawls at 1.0 / 1.2 / 1.4 mm, 2 latch rings", "PETG", "3 g", "~25 min", "Detent stiffness, cover latch"],
             ["3", "Deck, index cap, screw backing ring", "PLA", "60 g", "~6 h 30", "Ring journals, pawl pockets, cap"],
             ["4", "Outer ring, inner ring", "PLA", "30 g", "~3 h 10", "Ring fit, detent scallops"],
             ["5", "Same spring set in PLA + keystone; four fragments", "PLA", "9 g", "~1 h 10", "PLA vs PETG springs, fragment keying and clamp"],
             ["hold", "Flashlight bay corner of the base, door", "PLA", "16 g", "~1 h 30", "Only after caliper measurements"]],
            [10, 62, 16, 16, 18, 54]),
      Spacer(1, 5),
      P("<b>Bambu Studio settings</b> (0.4 mm nozzle, starting from the 0.20 mm Standard preset):", B),
      table([["Setting", "PLA plates", "PETG spring plate"],
             ["Wall loops", "3", "4, so the 1.0&ndash;1.4 mm springs are solid wall"],
             ["Top / bottom layers", "5 / 4", "default"],
             ["Infill", "15 % gyroid", "n/a"],
             ["Wall order", "Outer wall first on deck, rings, cover, seat test", "default"],
             ["Supports / brim", "Off / none", "Off / none"],
             ["Seam", "Aligned", "Aligned"],
             ["Plate", "Textured PEI", "Textured PEI"],
             ["Enclosure", "Door ajar or top glass off", "Closed; filament dried first"]],
            [40, 68, 68]),
      Spacer(1, 5),
      P("<b>Pass criteria</b>", B)]
s += bullets([
    "Cover drops in, turns to the stop without binding, lifts out; with the latch ring it clicks at both ends and stays in when inverted and shaken.",
    "Nut, once drawn in with a long screw, stays put with the latch ring removed.",
    "Mask slides down the well, clicks onto its ledge, survives inversion, pushes out from the back, arms intact after 10 cycles.",
    "With pawls out and cap screws fully tight, both rings spin freely with no rocking or rubbing.",
    "With pawls in (PETG 1.2, PETG 1.4, PLA 1.2 in turn), every position settles by itself, one finger turns the ring, nothing moves when shaken; repeat after about 200 clicks.",
    "Each fragment fits only its own socket; all four are immovable with the keystone tight.",
])

s += [P("5. Hardware (verified against the model)", H2),
      P("The model computes and checks its own screw lengths on every build and warns if a screw would bottom out or "
        "fall short.", B),
      table([["Item", "Per unit", "Four units", "Model check"],
             ["M3 × 16 socket-head cap screw", "3", "12", "7.4 mm clearance stack (cap 2.4 + rib 3.0 + deck 2.0), 8.6 mm of thread in a 10.5 mm self-tapped pilot in the 12 mm base"],
             ["M3 × 8 socket-head cap screw", "1", "4", "Reaches 3.9 mm below the cover face with fragments fitted; nut spans 1.4&ndash;3.8 mm"],
             ["M3 plain hex nut, 5.5 AF × 2.4", "1", "4", "Captive in the cover"]],
            [52, 16, 18, 90]),
      P("M3 × 20 does not fit the current 12 mm base; the one outdated source comment saying so has been corrected. "
        "No magnets, washers, inserts or glue are required.", B),

      P("6. Materials plan", H2),
      table([["Filament", "Parts", "One unit", "Four units", "To have (spares, 25 % failures, prototype)"],
             ["Antique brass PLA, metallic-effect, not silk", "Base, deck, index cap, cover, door", "101 g", "406 g", "~700 g"],
             ["Matte charcoal PLA", "Outer ring, keystone, mask", "22 g", "89 g", "~150 g"],
             ["Matte ivory PLA", "Inner ring, four fragments", "16 g", "65 g", "~110 g"],
             ["PETG, any dark colour", "Four detent springs, latch ring", "1.2 g", "5 g", "~20 g"]],
            [52, 50, 18, 20, 36]),
      P("Nothing has been purchased. The owner's filament inventory is unverified. Fit-critical parts (deck, cover, "
        "rings, springs) will be reprinted once in the final filaments and re-tested before the batch.", B),

      P("7. Open items", H2),
      table([["Item", "Owner", "Blocks"],
             ["Caliper measurements of the UV light (length with and without LED, greatest width, greatest thickness incl. switch dome, edge thickness, LED diameter, where a squeeze activates it). Bay is currently sized from photos: 43.5 × 23 × 8.5 mm, ±1 mm", "Owner, tonight", "Bay/door test print; full base"],
             ["Filament and hardware inventory check; purchases", "Owner", "Final-material test; production"],
             ["Round-1 test prints and feedback", "Owner", "Parameter tuning; instrument no. 1"],
             ["Parameter changes from test feedback; re-export", "Designer", "Next print round"],
             ["Final symbol set, clue sheets, real code and aperture positions", "Owner (game design)", "Labels, masks and fragments for production"],
             ["Surface decoration", "Deferred", "Nothing &mdash; explicitly out of scope until mechanisms are frozen"]],
            [96, 34, 46]),

      P("8. Production plan (after tests pass)", H2)]
s += bullets([
    "<b>Step 0:</b> reprint deck, cover, both rings and springs in the final filaments; repeat the checks. These become instrument no. 1.",
    "<b>Step 1:</b> complete instrument no. 1, play-test it with real labels and a full-size clue sheet, then freeze.",
    "<b>Step 2:</b> batch the other three plus spares on nine single-filament plates, two 125 mm parts per plate: "
    "decks, outer rings, inner rings, PETG springs, remaining deck + index caps, remaining ring + keystones + masks, "
    "bases (overnight), last base + covers + doors (overnight), fragments. About 52 h of printing by the generic "
    "estimate; about 67 h if no. 1 must be reprinted.",
    "<b>Spares:</b> two extra spring sets per unit, 4 latch rings, 4 masks, 2 doors, 1 cover, 1 keystone, 1 inner ring, 1 fragment set.",
    "<b>Schedule:</b> days 14&ndash;12 before the event for round-1 tests; 11&ndash;9 for the UV test, material check and "
    "instrument no. 1; day 8 freeze; days 7&ndash;3 for the batch at about two plates a day; days 2&ndash;1 for assembly, "
    "labels and a full play-test. About two days of slack.",
    "<b>Fallbacks already in the model:</b> remove the flashlight bay and door (light issued as a separate prop; the UV "
    "disc puzzle is unaffected); loose keyed drop-in mask with a finger notch.",
])

s += [P("9. Questions for the reviewer", H2)]
s += bullets([
    "Is the test order right, or should something else be proven first?",
    "Do the five test plates isolate each mechanism well enough to diagnose a failure, or is a variable confounded?",
    "Are the Bambu Studio settings appropriate, in particular outer-wall-first on the journals and 4 walls for the springs?",
    "Is testing fits in arbitrary PLA and then re-testing in the final filaments a sound approach, or a wasted round?",
    "Which of the 'still to be proven' items in section 3 do you expect to fail, and what would you prepare in advance?",
    "Is the latch (retaining ring doubling as a spring) likely to be strong enough, and what would you change first if it is not?",
    "Is about two days of slack enough for four units, and at what point should the flashlight compartment be dropped?",
    "Is anything missing from the open-items list?",
])

s += [P("10. Files", H2),
      P("Source: <font face='Courier'>cad/chronometer.scad</font> (single parametric file). Supporting documents in the "
        "same repository: <font face='Courier'>docs/PRINT_PLAN.md</font> (full test and production plan), "
        "<font face='Courier'>docs/MATERIALS.md</font> (materials and purchasing analysis), "
        "<font face='Courier'>docs/DESIGN_REVIEW.md</font> (design reasoning), and "
        "<font face='Courier'>docs/Chronometer_design_handoff.pdf</font> (detailed design description with all renders). "
        "Attach any of these if the reviewer should go deeper.", B)]


def footer(canvas, doc):
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillGray(0.4)
    canvas.drawString(18 * mm, 10 * mm, "The Chronometer - status handoff - CAD complete, nothing printed yet")
    canvas.drawRightString(letter[0] - 18 * mm, 10 * mm, "page %d" % doc.page)


SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm,
                  bottomMargin=17 * mm, title="The Chronometer - status handoff").build(
    s, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "kB")
