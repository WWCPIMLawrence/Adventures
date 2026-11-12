#!/usr/bin/env python3
"""Builds docs/Chronometer_symbol_test_handoff.pdf - the printed dial-symbol experiment, for an outside reviewer."""
import os
from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "Chronometer_symbol_test_handoff.pdf")
SRC = os.path.join(ROOT, "images", "symbol_test.png")
ANN = os.path.join(ROOT, "images", "symbol_test_labelled.png")
NAMES = "SUN MOON KEY FLAME STAR WAVE MOUNTAIN HOURGLASS TREE COMPASS DIAMOND EYE".split()

# labelled close-up of the two flush rows (render scale: 12.5 px per mm, first symbol at x=271, pitch 125.6)
im = PILImage.open(SRC).convert("RGB").crop((180, 110, 1760, 400))
im = im.resize((im.width * 1, im.height * 1))
canvas_im = PILImage.new("RGB", (im.width, im.height + 60), "white")
canvas_im.paste(im, (0, 60))
d = ImageDraw.Draw(canvas_im)
fp = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
f = ImageFont.truetype(fp, 20) if os.path.exists(fp) else ImageFont.load_default()
for i, n in enumerate(NAMES):
    d.text((271 - 180 + i * 125.6, 30), n, fill="black", font=f, anchor="mm")
canvas_im.save(ANN)

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


s = [P("The Chronometer &mdash; printed dial-symbol test", H1),
     P("The owner would like the twelve symbols on the Chronometer's inner dial to be 3D-printed into the ring "
       "instead of applied as adhesive labels. This document describes a small test plate made to find out "
       "whether that is legible and practical. <b>The plate has not been printed yet, and the production model "
       "has not been changed</b>: the test is a separate CAD file and the inner ring keeps its label pockets.", B),
     Spacer(1, 3),
     P("<b>To the reviewer (ChatGPT).</b> Please assess the symbol designs for legibility at 6 mm, the test method, "
       "and the two-colour printing plan. Questions are in section 7.", B),

     P("1. Context and constraints", H2)]
s += bullets([
    "Inner dial ring: matte bone-white PLA (SUNLU Matte Bone White), Ø83 mm, printed face up. Twelve positions, each "
    "with a label area about 9 mm wide radially and 14 mm along the arc, separated by raised finger ribs.",
    "Symbols, clockwise from XII: sun, moon, key, flame, star, wave, mountain, hourglass, tree, compass, diamond, eye. "
    "The sun is the setting symbol; moon, star, hourglass and diamond are the four that are read for the final code.",
    "Printer: Bambu Lab P1S with AMS, 0.4 mm nozzle, 0.20 mm layers. Matte black PLA is on hand.",
    "The owner has a colour laser printer, not an inkjet, so the earlier inkjet-vinyl label plan is out.",
    "Not to be touched: the ring's bore, flange, detent scallops and outside dimensions.",
])

s += [P("2. The symbols", H2),
      Image(ANN, width=176 * mm, height=176 * mm * 350 / 1580),
      P("CAD render of the two flush rows: 6 mm symbols above, 7 mm below. Left to right is clockwise on the dial.", CAP),
      Spacer(1, 3),
      P("Design rule: at the 6 mm size every solid stroke is at least 0.6 mm wide and every gap at least 0.5 mm, "
        "so each feature is at least one and a half nozzle widths. The six shapes the owner flagged as most likely "
        "to be confused were made structurally different:", B),
      table([["Symbol", "Distinguishing structure"],
             ["Star", "Five points, solid"],
             ["Diamond", "Tall solid rhombus, four corners, nothing around it"],
             ["Compass", "Ring with a slim needle inside"],
             ["Mountain", "Wide flat base, two unequal peaks"],
             ["Tree", "Rounded canopy on a trunk with a ground bar"],
             ["Flame", "Teardrop with a side tongue and a hollow centre"]], [40, 136]),

      P("3. The test plate", H2),
      P("One plate, 136 × 53 × 2 mm, printed face up exactly as the ring prints. Two STL files loaded as one object "
        "with two parts: the bone-white body and the black inlays.", B),
      table([["Row", "Approach", "Symbol size", "Purpose"],
             ["1", "Flush two-colour inlay, 0.4 mm deep (two layers of black)", "6 mm", "The intended size"],
             ["2", "Flush two-colour inlay, 0.4 mm deep", "7 mm", "Whether slightly larger reads clearly better; 7 mm still fits the label area"],
             ["3", "Recessed 0.4 mm, left open", "6 mm", "Paint-fill, shallow"],
             ["4", "Recessed 0.6 mm, left open", "6 mm", "Paint-fill, deeper"]], [12, 74, 24, 66]),
      Spacer(1, 3),
      P("Sliced weight 17 g; about 2&frac14; hours by a generic PrusaSlicer profile, plus the filament changes. "
        "Bambu Studio settings: 0.20 mm layers, 3 walls, top shell 5 layers, monotonic top surface, <b>ironing off</b>, "
        "prime tower on, flushing volumes on auto-calculate, textured PEI.", B),

      P("4. What will be judged on the print", H2)]
s += bullets([
    "Each of the twelve named correctly at arm's length in ordinary indoor light, by someone who has not seen the list.",
    "6 mm against 7 mm.",
    "Fine features: sun rays, key teeth, eye outline, compass needle, flame hollow.",
    "Flush rows: black smeared into white, white specks in black, inlays standing proud or sunken.",
    "Recessed rows, half of each painted: does wiping stain the matte white, and is 0.4 mm deep enough?",
])

s += [P("5. Estimates for four complete rings", H2),
      P("Estimates only. The base ring time is slicer-measured (generic profile); purge figures are a rough range "
        "until Bambu Studio reports the flushed weight for these two spools on the test plate.", B),
      table([["", "Flush two-colour (AMS)", "Recessed + paint-fill"],
             ["Filament changes", "About 2&ndash;4 for the whole plate. The symbols are only in the top two layers, and the count is per plate, so four rings on one plate cost the same as one", "None"],
             ["Purge waste", "Very roughly 1&ndash;4 g plus a small prime tower, for all four rings together. Black-to-white is the expensive direction", "None"],
             ["Black in the symbols", "Under 0.1 g per ring", "&mdash;"],
             ["Print time, four rings", "About 4 h 40 plus 5&ndash;10 min for the changes", "About 4 h 40"],
             ["Hand work", "None", "Perhaps 10&ndash;15 min per ring plus drying"],
             ["Main risk", "Colour smear on the top surface", "Paint staining the matte surface; wear from fingers"]],
            [34, 86, 56]),
      Spacer(1, 3),
      P("Expectation, unconfirmed: the flush inlay should be crisper and more durable, and is nearly free in purge "
        "when all four rings share a plate. Paint-fill is the fallback if the AMS result is smeared.", B),

      P("6. If the test passes", H2)]
s += bullets([
    "The symbols go on the top face of the inner ring, between the finger ribs, replacing the label pockets. That face "
    "is not a mating surface, so the bore, flange, detent scallops and outside dimensions are unchanged.",
    "The label-pocket ring stays in the model as a switchable fallback.",
    "If printed symbols are not adopted, the sticker sheet still applies, but on laser-compatible matte label stock.",
    "This experiment runs alongside the mechanical fit tests and does not change them.",
])

s += [P("7. Questions for the reviewer", H2)]
s += bullets([
    "Looking at the render, is any symbol likely to be misread at 6 mm, or mistaken for another? Which would you redraw?",
    "Are the four read symbols (moon, star, hourglass, diamond) and the setting symbol (sun) the most unmistakable of the twelve, as they should be?",
    "Is a 0.4 mm (two-layer) black inlay enough for a clean, opaque top surface in matte PLA, or would you use three layers?",
    "Any better way to keep black from smearing into bone white on a top surface than turning ironing off?",
    "Is the purge estimate plausible for a black/bone-white pair, and is there a setting that reduces it safely?",
    "For paint-fill on matte PLA, what filler and method would you use to avoid staining the surface?",
    "Is anything missing from the evaluation checklist in section 4?",
])
s += [P("8. Files", H2),
      P("<font face='Courier'>cad/symbol_test.scad</font> (stand-alone source), "
        "<font face='Courier'>stl/symbol_test_body.stl</font>, <font face='Courier'>stl/symbol_test_inlay.stl</font>, "
        "<font face='Courier'>docs/SYMBOL_TEST.md</font> (print instructions).", B)]


def footer(c, doc):
    c.setFont("Helvetica", 7.5); c.setFillGray(0.4)
    c.drawString(18 * mm, 10 * mm, "The Chronometer - printed dial-symbol test - not yet printed, production model unchanged")
    c.drawRightString(letter[0] - 18 * mm, 10 * mm, "page %d" % doc.page)


SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm, bottomMargin=17 * mm,
                  title="The Chronometer - printed dial-symbol test").build(s, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT)
