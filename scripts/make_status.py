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
       "26 November 2026. Four identical units, Bambu Lab P1S with AMS, PLA and PETG, M3 hardware. This document "
       "supersedes the earlier status handoffs.", B),
     Spacer(1, 4),
     P("<b>To the reviewer.</b> Physical prototyping is well under way. Please check the remaining plan and "
       "risks. Questions are in section 9. Dimensions are millimetres.", B),

     P("1. Status in one paragraph", H2),
     P("Every mechanism has now passed on a printed test piece: mask, nut pocket, cover twist-lock and latch, both "
       "rings and their detents, the index-cap screws, the flashlight compartment and its door, and the fragments "
       "with their centre knob. Several needed one to four design revisions to get there; those are listed in "
       "section 3. Raised two-colour lettering passed on a test plate and is now built into both rings. "
       "<b>No complete instrument has been assembled yet.</b> The full base is printing now; the deck and the two "
       "lettered rings follow. Test parts so far are in black PLA; the brass-coloured filament has not arrived. "
       "No production batch has been started.", B),
     Spacer(1, 4),
     pair("fn1_top.png", "Current CAD, top view: raised bone-white numerals on the black ring, raised black symbols and ribs on the bone-white ring.",
          "fn0_as_issued.png", "Current CAD, as issued to players. Flat-colour preview, not a photograph."),

     P("2. Test results on printed parts", H2),
     table([["Feature", "Result", "Setting that passed"],
            ["Aperture mask", "Pass", "Spring arms click into the well; stays in when inverted; pushes out from the back"],
            ["Captive nut in the cover", "Pass", "Drawn in with a screw past an undersized pocket mouth; stays put"],
            ["Cover twist-lock", "Pass", "0.75 mm axial play at entry, 0.50 mm locked: turns easily, no wiggle"],
            ["Cover latch", "Pass", "PETG ring 2.1 mm thick, 1.1 mm groove with steep sides: clear click at both ends"],
            ["Rings on the deck", "Pass", "0.30 mm radial clearance, 0.35 mm axial play; both spin and sit flat"],
            ["Detents", "Pass", "1.4 mm PETG leaf springs: both rings click at all 12 positions"],
            ["Index-cap screws", "Pass", "Pan-head self-tapping screws, about 3 × 16 mm, into printed 2.8 mm pilots"],
            ["Flashlight fit", "Pass", "Bay 42.3 × 24.1 × 10.2 for a 40.3 × 22.6 × 8.7 light; loose in plan, to be lined with felt"],
            ["Door slide, latch and rim", "Pass", "V-shaped rails, catch on an in-plane spring, upright rim tab on the door"],
            ["Fragments and centre knob", "Pass", "Each fragment fits one socket only; all four lock under the knob"],
            ["Raised lettering", "Pass on a plate", "0.4 mm high, 7 mm symbols and numerals, one filament change; clear at arm's length"],
            ["Lettering on the actual rings", "Not yet printed", "&mdash;"],
            ["Complete instrument", "Not yet assembled", "&mdash;"],
            ["Aperture sheet read through the well", "Not yet tested", "&mdash;"],
            ["Fits in the final brass filament", "Not yet tested", "Filament not delivered"]],
           [46, 26, 104]),

     P("3. What had to change during testing", H2),
     table([["Part", "What happened on the print", "Fix"],
            ["Cover twist-lock", "Bound through the whole turn at 0.45 / 0.30 mm play; over-corrected to 0.90 / 0.70 (about 1 mm of lift); 0.70 / 0.40 bound again", "Two seat variants printed side by side settled it at 0.75 / 0.50. The two facing 45&deg; overhangs droop by roughly 0.4 mm"],
            ["Cover latch", "No click with a 1.6 mm ring and 0.7 mm groove; faint at 1.8 / 0.9", "2.1 mm ring, 1.1 mm groove, steeper groove sides"],
            ["Door latch", "Three progressively stronger catches all gave almost no resistance", "Root cause was the rails, not the catch: on a plain dovetail the door could lift into the body and free the catch. V-shaped rails (widest at mid-thickness) stop it lifting"],
            ["Ceiling over the door channel", "A 29 mm flat bridge strung and sagged; a 0.5 mm unsupported ledge fell away", "Channel roof now rises at 45&deg; to the base top, which the deck closes. No flat bridge"],
            ["Rim above the door", "The bridged rim strip drooped visibly; later a thin 27&deg; sliver broke off", "That piece of rim is now an upright tab on the door, with a square end"],
            ["Centre knob", "M3 × 8 screw hard to start in the nut", "Screw bore deepened by 0.8 mm"],
            ["Symbol test, first attempt", "Two-part file loaded as separate objects; plate printed in one colour without its inlay", "Replaced by a single file with raised lettering and a filament change at one layer"],
            ["Order of walls", "The designer asked for inner-first; all passing parts were in fact printed outer/inner", "Outer/inner is now the documented setting, since the fits are calibrated to it"]],
           [34, 70, 72]),

     P("4. Design as it now stands", H2)]
s += bullets([
    "<b>Size:</b> Ø125, 19.8 thick at the rim, about 30 over the centre knob. Base 12.2, deck 5.0.",
    "<b>Two dials</b> with 12 detented positions each, read against a fixed arrow at XII; trapped by one index cap on three screws.",
    "<b>Centre cover:</b> three-lug twist-lock, 28&deg; turn, held shut by a sprung nub on the PETG retaining ring inside the cover.",
    "<b>Aperture:</b> interchangeable stencil at the bottom of a 50 mm well, four Ø10.5 apertures.",
    "<b>UV light:</b> lies flat in a bay in the base behind a sliding door in the back face. The door runs on V-shaped "
    "rails, carries the strip of rim above its opening as an upright tab, and has a side-spring catch. The light goes "
    "in with its slide-lock tab away from the door and its LED toward the closed end.",
    "<b>Fragments:</b> four keyed tiles dock on the cover face and are clamped by a centre thumb-knob.",
    "<b>Lettering:</b> raised 0.4 mm. Outer ring black with bone-white numerals; inner ring bone white with black symbols "
    "and finger ribs. One filament change per ring, at layer 29. Sticker pockets and engraved numerals remain as fallbacks.",
])

s += [P("5. Game configuration (approved, unchanged)", H2),
      P("Final answer 1147. Code ring clockwise from XII: 813619245072; fragments read 281 / 361 / 924 / 507. Dial "
        "symbols clockwise from XII: sun, moon, key, flame, star, wave, mountain, hourglass, tree, compass, diamond, "
        "eye. Set the sun to the arrow, then read moon, star, hourglass, diamond. Aperture word RIFT. UV disc: "
        "\"THE SUN IS FALSE. TRUST THE ARROW.\" The UV text and the 6 / 9 decoys have not yet been checked on real parts.", B),

      P("6. Print settings in use", H2),
      table([["Setting", "Value"],
             ["Preset", "0.20 mm Standard, 0.4 mm nozzle, saved as a project preset"],
             ["Changes from default", "Order of walls outer/inner; wall loops 3; bottom shell layers 4; gyroid infill at 15 %; no brim"],
             ["Unchanged", "Top shell layers 5, aligned seam, no ironing, classic wall generator, supports off, prime tower on"],
             ["PETG springs and latch ring", "Same preset with wall loops 4"],
             ["Rings", "Filament change at layer 29"],
             ["Measured speed", "Full base slices at 1 h 27 min on the P1S, about a third of the designer's generic estimate"]],
            [44, 132]),

      P("7. Colours and hardware", H2),
      table([["Filament", "Parts"],
             ["Brass-coloured PLA (ERYONE, non-silk), on order", "Base, deck, index cap, centre cover, door"],
             ["Matte black PLA, on hand", "Outer ring body, mask, centre knob, inner-ring symbols"],
             ["SUNLU Matte Bone White PLA, on hand", "Inner ring body, fragments, outer-ring numerals"],
             ["Dark PETG, on hand", "Four detent springs, latch ring"]],
            [70, 106]),
      P("Hardware per unit: three self-tapping screws of about 3 × 16 mm (or M3 × 16 socket-head), one M3 × 8 "
        "socket-head screw, one plain M3 nut. The owner has enough of all three.", B),

      P("8. What remains", H2),
      table([["Step", "Owner", "State"],
             ["Print base, deck and both lettered rings; assemble one complete instrument", "Owner", "Base printing now"],
             ["Check rings, cover, door and rim alignment on the full assembly; read the aperture sheet through the well", "Owner", "Next"],
             ["Decide fragment digit colouring: black-faced tiles with ivory digits from one filament change, or ivory tiles with paint-filled digits", "Owner", "Open"],
             ["UV marker test on the practice disc; brightener-free paper", "Owner", "Open"],
             ["When the brass filament arrives: reprint cover and one seat piece to confirm the twist-lock, then base, deck, index cap, cover, door", "Owner", "Waiting on delivery"],
             ["Issue the master file set once the full instrument passes", "Designer", "After assembly test"],
             ["Batch three more instruments plus spares (about 17 h of printing at measured speed)", "Owner", "After freeze"]],
            [112, 26, 38]),

      P("9. Questions for the reviewer", H2)]
s += bullets([
    "The fits were calibrated in black PLA. What is the most efficient way to re-check them in the brass filament, and which fit is most likely to shift?",
    "The door now carries a 3 mm upright rim tab on a 2 mm plate. Is that tab likely to snap in handling, and would you reinforce it?",
    "With raised lettering, the inner ring's finger ribs print in the lettering colour. Is that acceptable visually, or should the ribs be lowered to the ring face?",
    "Fragment digits print face-down and cannot be raised. Which of the two colouring options is more robust?",
    "Is there anything in the full-assembly test that should be checked and is missing from section 8?",
    "Given measured print speed, is it worth printing a second complete instrument in final colours before batching the last two?",
])

s += [P("10. Files", H2),
      P("Source: <font face='Courier'>cad/chronometer.scad</font> (single parametric file). Lettering test: "
        "<font face='Courier'>cad/symbol_test.scad</font>. Supporting documents: "
        "<font face='Courier'>README.md</font> (results table, assembly, parameters), "
        "<font face='Courier'>docs/PRINT_PLAN.md</font>, <font face='Courier'>docs/MATERIALS.md</font>, "
        "<font face='Courier'>docs/SYMBOL_TEST.md</font>. Where earlier handoffs differ, this document is current.", B)]


def footer(canvas, doc):
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillGray(0.4)
    canvas.drawString(18 * mm, 10 * mm, "The Chronometer - status handoff - mechanisms proven on test prints, full assembly pending")
    canvas.drawRightString(letter[0] - 18 * mm, 10 * mm, "page %d" % doc.page)


SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm,
                  bottomMargin=17 * mm, title="The Chronometer - status handoff").build(
    s, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "kB")
