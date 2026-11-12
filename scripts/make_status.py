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
     P("A 3D-printed mechanical puzzle instrument for a family scavenger hunt, <i>The Timekeeper's Paradox</i>, on "
       "26 November 2026. Four identical units, Bambu Lab P1S with AMS, PLA/PETG, M3 hardware. This document "
       "replaces the earlier status handoff and reflects everything decided since.", B),
     Spacer(1, 4),
     P("<b>To the reviewer.</b> Please check the plan and the open risks, not just the design. Questions are in "
       "section 10. All dimensions are millimetres.", B),

     P("1. Status in one paragraph", H2),
     P("The design is complete in CAD and has had one outside mechanical review, applied in full. The game "
       "configuration is approved and applied to the fragments and printed sheets. The UV flashlight has now been "
       "measured with calipers and its compartment resized. A separate test plate for printing the dial symbols "
       "into the ring is ready. Twenty-two automated geometry checks pass. <b>Nothing has been printed or "
       "physically tested yet</b>; no full instrument and no batch of four will be printed until the fit tests pass.", B),
     Spacer(1, 4),
     pair("fn0_as_issued.png", "As issued to players (flat-colour CAD preview, no decoration yet).",
          "exploded.png", "Exploded view: 18 printed parts, 4 screws, 1 nut."),

     P("2. What is new since the last status handoff", H2),
     table([["Item", "Then", "Now"],
            ["UV flashlight size", "Estimated from photos: 43.5 × 23 × 8.5", "Caliper-measured, key ring removed: <b>40.3 long (LED included) × 22.6 wide × 8.7 thick</b>"],
            ["Flashlight compartment", "On hold", "Resized to 42.3 × 24.1 × 10.2 (1 mm free at each end, 1.5 mm total at sides and faces); moved 1 mm in from the rim; thinnest walls now 3.2&ndash;3.6 mm (were 2.3&ndash;2.9). Fit-test piece released for printing; full base still on hold"],
            ["Overall height", "19.6 at the rim", "19.8 at the rim, 29.8 over the centre knob (base is 12.2 tall)"],
            ["Game configuration", "Demo values (TIME, 1847)", "Approved and applied &mdash; section 4"],
            ["Dial symbols", "Adhesive labels only", "Printed-symbol test plate prepared &mdash; section 5. Labels remain the fallback"],
            ["Label stock", "Inkjet vinyl assumed", "Owner has a colour laser printer: laser-compatible matte labels only, if labels are used"],
            ["Hardware", "M3 × 16, M3 × 8, nut", "Unchanged and re-verified: M3 × 16 has 8.6 mm of thread in a 10.7 mm pilot; the model checks screw lengths on every build"]],
           [38, 46, 92]),

     P("3. The instrument, briefly", H2)]
s += bullets([
    "<b>Two dials:</b> an outer hour ring (the knurled rim) and an inner symbol ring, 12 detented positions each, read "
    "against a fixed arrow at XII. Both are trapped by one fixed index ring held by three screws.",
    "<b>Detents:</b> four separate arc-shaped leaf springs in pockets of a fixed rib, two per ring; PETG planned.",
    "<b>Centre cover:</b> three-lug twist-lock, 28&deg; turn, loose running fit (0.30 mm axial play locked). A sprung nub "
    "on the UV retaining ring inside the cover clicks into a groove in the well wall to hold it shut.",
    "<b>Aperture:</b> an interchangeable stencil at the bottom of a 50 mm well, 0.8 mm above the paper, four Ø10.5 apertures.",
    "<b>UV:</b> the flat squeeze-type light lies in a bay in the base behind a flush sliding door in the back face. "
    "The UV-reactive paper disc lives inside the centre cover.",
    "<b>Final code:</b> four keyed fragments dock on the cover face, clamped by a centre thumb-knob whose cone seats "
    "on their bevels. They form a 12-character ring read against the inner dial.",
])

s += [P("4. Approved game configuration (applied; no mechanical geometry changed)", H2),
      table([["Element", "Approved value", "Verification"],
             ["Final answer", "1147 (11:47)", "Sheet generator refuses to build unless the four read symbols give 1147"],
             ["Code ring, clockwise from XII", "813619245072", "&mdash;"],
             ["Fragment tiles 1&ndash;4", "281 / 361 / 924 / 507", "Follows from the existing socket positions (tiles centred on XII, III, VI, IX). Decoy 6 and 9 kept pending a readability check on printed tiles"],
             ["Dial symbols, clockwise from XII", "Sun, moon, key, flame, star, wave, mountain, hourglass, tree, compass, diamond, eye", "Sun is the setting symbol"],
             ["Reading rule", "Sun at the arrow; read moon, star, hourglass, diamond", "Positions I, IV, VII, X. One click off reads 3952 or 8620; sun at III, VI or IX gives 1471, 4711, 7114, none a valid time"],
             ["Aperture word", "RIFT", "Reads cleanly for placement errors up to 1.7 mm (geometric check)"],
             ["UV disc text", "\"THE SUN IS FALSE. TRUST THE ARROW.\"", "Fits the writable circle as four lines of 4 mm capitals, by calculation. <b>Not yet tested with the real marker</b>; a practice disc is on the template sheet"],
             ["Final instruction (given separately)", "\"Place the false hour beneath the arrow. Then read the records in the order they were witnessed: Moon, Star, Hourglass, Diamond.\"", "&mdash;"]],
            [40, 62, 74]),

      P("5. Printed dial-symbol experiment", H2),
      Image(os.path.join(IMG, "symbol_test_labelled.png"), width=176 * mm, height=176 * mm * 350 / 1580),
      P("CAD render of the two flush rows of the test plate: 6 mm symbols above, 7 mm below.", CAP)]
s += bullets([
    "Stand-alone test plate, 136 × 53 × 2, SUNLU Matte Bone White body with matte black inlays. Rows: flush two-colour "
    "at 6 mm, flush two-colour at 7 mm, recessed 0.4 mm and recessed 0.6 mm for paint-fill. Inlay depth 0.4 mm (two "
    "layers), ironing off, Bambu Studio's calculated flushing volumes.",
    "Every stroke is at least 0.6 mm and every gap at least 0.5 mm at the 6 mm size. Three symbols were corrected to "
    "meet that rule (compass needle shortened, eye pupil reduced, hourglass waist widened).",
    "<b>7 mm is the preferred size and fits the ring:</b> 1.0 mm radial margin inside the label area, 1.8 mm to the edge "
    "of the ring face, 3.7 mm clearance to each finger rib.",
    "Estimate for four rings on one plate: 2&ndash;4 filament changes in total, very roughly 1&ndash;4 g of purge plus a "
    "small prime tower, about 4 h 40 of printing. Estimates until Bambu Studio reports the flushed weight.",
    "If the 7 mm two-colour symbols are clean and legible, they become the production approach as a switchable option; "
    "they occupy only the top 0.4 mm of the ring face, so no mating surface changes. The production model is unchanged "
    "until then.",
])

s += [P("6. Print queue", H2),
      P("Any ordinary PLA for prints 1, 3, 4, 5 and 6; any PETG for print 2. Weights and times are from PrusaSlicer "
        "with a generic profile, not Bambu Studio.", B),
      table([["#", "Parts", "Filament", "Weight", "Time", "Tests"],
             ["1", "Seat test piece, cover, mask", "PLA", "22 g", "~2 h 20", "Twist-lock through its full turn, latch grooves, mask retention"],
             ["2", "Spring plate: pawls at 1.0 / 1.2 / 1.4 mm, 2 latch rings", "PETG", "3 g", "~25 min", "Detent stiffness, cover latch"],
             ["3", "Deck, index cap, screw backing ring", "PLA", "60 g", "~6 h 30", "Ring journals, pawl pockets, cap"],
             ["4", "Outer ring, inner ring", "PLA", "30 g", "~3 h 10", "Ring fit, detent scallops"],
             ["5", "PLA spring set + keystone; four fragments (approved characters)", "PLA", "9 g", "~1 h 10", "PLA vs PETG springs, fragment keying and clamp, 6/9 readability"],
             ["6", "Flashlight bay corner of the base, door", "PLA", "17 g", "~1 h 30", "Light fit, accidental switch-on, door slide and click, bridge sag"],
             ["7", "Symbol test plate (two parts, two colours)", "Bone white + black PLA", "17 g", "~2 h 15 + changes", "Symbol legibility at 6 and 7 mm; flush vs paint-fill"]],
            [8, 62, 26, 14, 22, 44]),
      Spacer(1, 3),
      P("Settings: 0.20 mm layers, 0.4 mm nozzle, 3 walls, 5 top / 4 bottom layers, 15 % gyroid, outer wall first on "
        "the deck, rings, cover and seat piece, no supports, no brim, aligned seam, textured PEI. PETG spring plate: "
        "4 walls so the springs are solid. Symbol plate: monotonic top surface, ironing off, prime tower on.", B),

      P("7. Materials and hardware", H2),
      table([["Filament", "Parts", "Four units", "To have (spares, 25 % failures, prototype)"],
             ["Antique brass PLA, metallic-effect, not silk", "Base, deck, index cap, cover, door", "~410 g", "~700 g"],
             ["Matte charcoal PLA", "Outer ring, keystone, mask", "89 g", "~150 g"],
             ["Matte ivory / bone PLA (SUNLU Matte Bone White on hand)", "Inner ring, four fragments", "65 g", "~110 g"],
             ["PETG, any dark colour", "Four detent springs, latch ring", "5 g", "~20 g"],
             ["Matte black PLA (on hand)", "Dial symbols, if adopted", "under 0.5 g", "a few grams with purge"]],
            [58, 46, 22, 50]),
      P("Hardware per unit: 3 × M3 × 16 and 1 × M3 × 8 socket-head cap screws, 1 plain M3 hex nut. The owner is still "
        "checking filament and hardware inventory; nothing has been purchased on the designer's advice.", B),

      P("8. Open items", H2),
      table([["Item", "Owner", "Blocks"],
             ["Print and report on queue items 1&ndash;7", "Owner", "All tuning; instrument no. 1"],
             ["UV marker legibility on the practice disc; brightener-free paper", "Owner", "Final UV discs"],
             ["Whether a squeeze anywhere on the light's face switches it on; LED protrusion", "Owner", "Nothing unless the light switches on in test 6"],
             ["Filament and hardware inventory; purchases", "Owner", "Final-material re-test; production"],
             ["Parameter changes from test feedback; re-export", "Designer", "Next print round"],
             ["Printed-symbol ring option in the production model", "Designer, after test 7 passes", "Inner rings for production"],
             ["Decoy 6 / 9 decision; final symbol artwork", "Owner, after prints", "Final fragments and labels or symbols"],
             ["Surface decoration", "Deferred", "Nothing"]],
            [96, 40, 40]),

      P("9. Production plan (unchanged; starts only after the tests pass)", H2)]
s += bullets([
    "Reprint deck, cover, both rings and springs once in the final filaments and repeat the checks; these become instrument no. 1.",
    "Complete instrument no. 1, play-test it with the real symbols and a full-size clue sheet, then freeze.",
    "Batch the other three plus spares on nine single-filament plates, mechanism parts first, bases and covers overnight: "
    "about 52 h by the generic estimate, about 67 h if no. 1 must be reprinted.",
    "Fallbacks already in the model: remove the flashlight bay and door (light issued as a prop); loose drop-in mask; "
    "label pockets instead of printed symbols.",
    "Schedule slack is about two days. The flashlight compartment is the piece to drop if a test round must be repeated.",
])

s += [P("10. Questions for the reviewer", H2)]
s += bullets([
    "With 1.5 mm total face clearance around an 8.7 mm squeeze light, is accidental switch-on still a realistic risk, and what would you check first?",
    "Should the symbol plate (print 7) run earlier in the queue, given that it decides how the inner rings are made?",
    "Is anything in the approved game configuration still ambiguous to a first-time player, for example which mark is \"the arrow\"?",
    "Is four lines of 4 mm capitals a reasonable target for hand lettering with a UV marker on a 42 mm disc?",
    "Which queued test do you expect to fail, and what should be prepared in advance?",
    "Is about two days of slack enough, and at what point should the flashlight compartment or the printed symbols be dropped?",
])

s += [P("11. Files", H2),
      P("Source: <font face='Courier'>cad/chronometer.scad</font>; symbol experiment: "
        "<font face='Courier'>cad/symbol_test.scad</font>. Supporting documents: "
        "<font face='Courier'>docs/PRINT_PLAN.md</font>, <font face='Courier'>docs/MATERIALS.md</font>, "
        "<font face='Courier'>docs/SYMBOL_TEST.md</font>, <font face='Courier'>docs/DESIGN_REVIEW.md</font>. Earlier "
        "handoffs (design, puzzle review, symbol test) remain valid for detail but predate the caliper measurements; "
        "where they differ, this document is current.", B)]


def footer(canvas, doc):
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillGray(0.4)
    canvas.drawString(18 * mm, 10 * mm, "The Chronometer - status handoff - CAD complete, nothing printed yet - supersedes the earlier status handoff")
    canvas.drawRightString(letter[0] - 18 * mm, 10 * mm, "page %d" % doc.page)


SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm,
                  bottomMargin=17 * mm, title="The Chronometer - status handoff").build(
    s, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "kB")
