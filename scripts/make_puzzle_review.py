#!/usr/bin/env python3
"""Builds docs/Chronometer_puzzle_review.pdf - compatibility review of the proposed game
configuration against the current CAD. Read-only: computes everything from the proposal."""
import math
import os

from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "Chronometer_puzzle_review.pdf")
DIAG = os.path.join(ROOT, "images", "puzzle_layout.png")

SYMS = "SUN MOON KEY FLAME STAR WAVE MOUNTAIN HOURGLASS TREE COMPASS DIAMOND EYE".split()
READ = ["MOON", "STAR", "HOURGLASS", "DIAMOND"]
PROPOSED = ["813", "619", "245", "072"]
RING = list("".join(PROPOSED))                       # clockwise from XII
HOURS = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]


def code(ring, shift=0, names=READ):
    return "".join(ring[(SYMS.index(s) + shift) % 12] for s in names)


# the CAD centres fragment n on XII / III / VI / IX: positions 3n-1, 3n, 3n+1
cad_ring_if_loaded_as_written = [None] * 12
for n, f in enumerate(PROPOSED):
    for j, ch in zip((-1, 0, 1), f):
        cad_ring_if_loaded_as_written[(3 * n + j) % 12] = ch
CAD_FRAGS = ["".join(RING[(3 * n + j) % 12] for j in (-1, 0, 1)) for n in range(4)]
assert code(RING) == "1147" and code(cad_ring_if_loaded_as_written) == "3952"
assert CAD_FRAGS == ["281", "361", "924", "507"]
NEXT_FOUR = "".join(RING[k] for k in (1, 2, 3, 4))


def font(size, bold=False):
    for p in ("/usr/share/fonts/truetype/liberation/LiberationSans-%s.ttf" % ("Bold" if bold else "Regular"),
              "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def diagram():
    W, H = 1500, 900
    im = PILImage.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)

    def dial(cx, cy, title, bounds_deg, frag_labels):
        d.text((cx, cy - 400), title, fill="black", font=font(26, True), anchor="mm")
        for r in (330, 250, 170, 95):
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline="black", width=2)
        for k in range(12):
            a = math.radians(90 - 30 * k)
            ux, uy = math.cos(a), -math.sin(a)
            hot = SYMS[k] in READ
            d.text((cx + 352 * ux, cy + 352 * uy), HOURS[k], fill=(120, 120, 120), font=font(18), anchor="mm")
            d.text((cx + 290 * ux, cy + 290 * uy), SYMS[k], fill=(170, 30, 30) if hot else "black",
                   font=font(15, hot), anchor="mm")
            if hot:
                r0 = 22
                x, y = cx + 210 * ux, cy + 210 * uy
                d.ellipse([x - r0, y - r0, x + r0, y + r0], fill=(255, 225, 150), outline=(170, 30, 30), width=2)
            d.text((cx + 210 * ux, cy + 210 * uy), RING[k], fill="black", font=font(30, True), anchor="mm")
        for b in bounds_deg:                                   # fragment boundaries
            a = math.radians(90 - b)
            d.line([cx + 95 * math.cos(a), cy - 95 * math.sin(a), cx + 250 * math.cos(a), cy - 250 * math.sin(a)],
                   fill=(30, 60, 170), width=5)
        for n, lab in enumerate(frag_labels):
            mid = (bounds_deg[n] + bounds_deg[(n + 1) % 4] + (360 if n == 3 else 0)) / 2
            a = math.radians(90 - mid)
            d.text((cx + 132 * math.cos(a), cy - 132 * math.sin(a)), lab, fill=(30, 60, 170), font=font(20, True), anchor="mm")
        d.polygon([(cx - 10, cy - 345), (cx + 10, cy - 345), (cx, cy - 332)], fill="black")

    dial(365, 460, "As proposed: tiles start at XII (needs a cover change)", [-15, 75, 165, 255],
         ["1: " + PROPOSED[0], "2: " + PROPOSED[1], "3: " + PROPOSED[2], "4: " + PROPOSED[3]])
    dial(1135, 460, "Current CAD: tiles centred on XII, III, VI, IX", [-45, 45, 135, 225],
         ["1: " + CAD_FRAGS[0], "2: " + CAD_FRAGS[1], "3: " + CAD_FRAGS[2], "4: " + CAD_FRAGS[3]])
    d.text((W / 2, H - 28), "Same 12-character ring in both. Red = the four symbols read; highlighted digits = 1-1-4-7. "
           "Blue = fragment boundaries and what each tile carries.", fill="black", font=font(18), anchor="mm")
    im.save(DIAG)


ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontSize=17, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontSize=12.5, spaceBefore=10, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle("B", parent=ss["BodyText"], fontSize=9.5, leading=13)
CAP = ParagraphStyle("CAP", parent=B, fontSize=8.5, textColor=colors.HexColor("#444444"), alignment=1)
CELL = ParagraphStyle("CELL", parent=B, fontSize=8.5, leading=10.5)


def P(t, st=B):
    return Paragraph(t, st)


def bullets(items):
    return [P("&bull;&nbsp; " + t) for t in items]


def table(rows, widths):
    t = Table([[P(c, CELL) for c in r] for r in rows], colWidths=[w * mm for w in widths], repeatRows=1)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#999999")),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 2),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                           ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e2d0"))]))
    return t


diagram()
align = [code(RING, k) for k in range(12)]
s = [P("The Chronometer &mdash; puzzle configuration review", H1),
     P("Review of the provisional game specification for <i>The Timekeeper's Paradox</i> against the current "
       "Chronometer CAD. <b>No CAD, STL or printed-sheet file was changed.</b> Everything below was computed from the "
       "proposal and the model's existing geometry. The mechanical test prints are unaffected and remain the priority.", B),
     Spacer(1, 3),
     P("<b>To the reviewer (ChatGPT).</b> Two items in the proposal need a decision from the game design side: the "
       "fragment groupings (section 2) and the wording of the UV clue (section 3). Please confirm or revise them; "
       "the questions are in section 6.", B),

     P("1. Verdict", H2),
     table([["Proposed item", "Result", "Note"],
            ["Final answer 1147", "Compatible", "The ring 813619245072 (clockwise from XII) reads 1147 with SUN at the arrow"],
            ["Twelve symbols in the given order", "Compatible", "Dial has exactly 12 label pockets; labels are paper, so this is print-only. Five symbols still need artwork"],
            ["Fragments 813 / 619 / 245 / 072", "<b>Mismatch</b>", "Assumes tiles start at XII. The CAD centres them on XII, III, VI, IX. Loaded as written they read 3952"],
            ["SUN at reference, read MOON, STAR, HOURGLASS, DIAMOND", "Compatible", "Those symbols sit at positions I, IV, VII, X"],
            ["Aperture word RIFT", "Compatible", "Four letters, four apertures; placement tolerance 1.7 mm (TIME was 1.4 mm)"],
            ["UV message text", "<b>Misleading and too long</b>", "&quot;The four that follow&quot; reads 1361; 72 characters do not fit the disc at marker size"]],
           [50, 32, 94]),

     P("2. Fragment groupings", H2),
     Image(DIAG, width=176 * mm, height=176 * mm * 900 / 1500),
     P("The same ring cut two ways. Left: the proposal. Right: the current model.", CAP),
     Spacer(1, 3),
     P("In the model, fragment 1 is centred on XII and carries positions XI, XII, I; fragment 2 carries II, III, IV; "
       "fragment 3 carries V, VI, VII; fragment 4 carries VIII, IX, X. The four read positions (I, IV, VII, X) are "
       "therefore the clockwise-last character of each tile, one per tile.", B)]
s += bullets([
    "<b>Recommended (no mechanical change):</b> keep the ring 813619245072 and let the model cut it. The physical "
    "tiles then carry <b>%s, %s, %s, %s</b>. The answer is still 1147. This is one parameter "
    "(<font face='Courier'>code_ring</font>) when the game is finalized." % tuple(CAD_FRAGS),
    "<b>Alternative:</b> keep the tiles literally as 813 / 619 / 245 / 072 by rotating the four sockets on the "
    "centre cover by one position (30&deg;). This changes a part that is about to be test-printed, so it is not "
    "recommended now.",
    "Either way, any game text that quotes a fragment's three characters must use the grouping actually built.",
])

s += [P("3. UV message", H2),
      P("Proposed: <i>&quot;THE SUN IS THE FALSE HOUR. SET IT FIRST. THEN READ THE FOUR THAT FOLLOW.&quot;</i>", B)]
s += bullets([
    "<b>Wrong four.</b> The four symbols that follow the SUN on the dial are MOON, KEY, FLAME, STAR. Reading those "
    "gives <b>%s</b>, not 1147. The intended four are every third symbol." % NEXT_FOUR,
    "<b>No destination.</b> &quot;Set it first&quot; does not say where. The fixed reference is the double arrow at XII.",
    "<b>Recommended wording:</b> name the symbols, in this message or in a separate clue, for example "
    "<i>&quot;THE SUN IS THE FALSE HOUR. SET IT TO THE ARROW. READ MOON, STAR, HOURGLASS, DIAMOND.&quot;</i>",
    "<b>Not recommended:</b> making &quot;the four that follow&quot; literally true by putting the code at positions I&ndash;IV. "
    "All four digits would then sit on fragments 1 and 2, and the other two fragments would not be needed.",
    "<b>Length.</b> 72 characters. The writable area of the disc is about 42 mm across with a 4 mm hole in the centre. "
    "Estimated, not tested: the longest line would need letters under 2 mm wide, too small for a UV marker. Shorten "
    "the text, split it into two rings of text, or use a fine-tip UV pen, and trial it on the printed disc template.",
])

s += [P("4. Behaviour at wrong settings", H2),
      P("Reading MOON, STAR, HOURGLASS, DIAMOND with the SUN at each of the twelve positions:", B),
      table([["SUN at"] + HOURS, ["Reads"] + align], [16] + [13.3] * 12),
      Spacer(1, 3)]
s += bullets([
    "One click either side of correct gives %s or %s." % (align[1], align[11]),
    "Because the read positions are three apart, SUN at III, VI or IX gives rotations of the answer: %s, %s, %s. "
    "None is a valid clock time, so only 1147 can be read as a time." % (align[3], align[6], align[9]),
])

s += [P("5. Smaller risks", H2)]
s += bullets([
    "<b>6 and 9.</b> Characters run around a ring, so on a loose tile 6 and 9 are indistinguishable. Here they are "
    "decoys (positions III and V) and never part of the correct reading. Replacing them with other digits removes "
    "the confusion at no cost.",
    "<b>Look-alike symbols.</b> Symbols print at about 6 mm. STAR, DIAMOND and COMPASS can resemble each other, and two "
    "of them are read symbols. Draw the compass as a circle with a needle. FLAME, TREE and MOUNTAIN also need "
    "clearly different silhouettes.",
    "<b>Artwork still needed:</b> KEY, FLAME, MOUNTAIN, TREE, COMPASS. The current demo label sheet has other shapes "
    "in those positions.",
    "<b>Fragment order pips.</b> Each tile has 1&ndash;4 small dots and is keyed to one socket, so players cannot mis-seat "
    "them; the game does not need to tell players where each fragment goes.",
])

s += [P("6. Decisions needed", H2)]
s += bullets([
    "Fragment grouping: accept tiles reading %s / %s / %s / %s (recommended), or require the cover change?" % tuple(CAD_FRAGS),
    "UV clue: which wording, and will the four symbols be named on the disc or in another clue?",
    "Will any other clue quote a fragment's characters or refer to &quot;the four that follow&quot;? If so it must be updated to match.",
    "Replace the decoy 6 and 9? If yes, with which digits (anything except changing positions I, IV, VII, X)?",
    "Is RIFT final, and should the clue sheet's decoy letters avoid spelling anything?",
])
s += [P("7. What happens next", H2),
      P("Nothing is regenerated until the mechanisms are frozen. At that point the final ring, symbol order, aperture "
        "word and UV text go in together and the fragments, dial labels, clue sheet and disc template are re-exported "
        "as one consistent set.", B)]


def footer(canvas, doc):
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillGray(0.4)
    canvas.drawString(18 * mm, 10 * mm, "The Chronometer - puzzle configuration review - provisional, no files changed")
    canvas.drawRightString(letter[0] - 18 * mm, 10 * mm, "page %d" % doc.page)


SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm,
                  bottomMargin=17 * mm, title="The Chronometer - puzzle configuration review").build(
    s, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT, "| alignments", align, "| CAD fragments", CAD_FRAGS)
