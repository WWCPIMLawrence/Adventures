#!/usr/bin/env python3
"""Generates the printable paper parts for the Chronometer prototype.

  sheets/aperture_test_sheet.pdf   clue sheet that must read T-I-M-E through the mask
  sheets/labels_and_templates.pdf  inner-ring symbol labels, UV insert discs,
                                   fragment template and the demo decoding card
  sheets/aperture_proof.png        simulated view through the mask (+ a 1 mm misplacement)

Geometry (aperture positions, code ring ...) is read from cad/chronometer.scad so
the paper always matches the CAD.  Print the PDFs at 100 % / "Actual size".

Requires: reportlab, pillow, and pdftoppm (poppler) for the proof image.
"""
import math
import os
import random
import re
import subprocess

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAD = open(os.path.join(ROOT, "cad", "chronometer.scad")).read()
OUT = os.path.join(ROOT, "sheets")
os.makedirs(OUT, exist_ok=True)


def scad_num(name):
    return float(re.search(rf"^{name}\s*=\s*([-\d.]+)\s*;", SCAD, re.M).group(1))


def scad_list(name):
    body = re.search(rf"^{name}\s*=\s*(\[.*?\]);", SCAD, re.M | re.S).group(1)
    return eval(body)  # plain numeric / string lists only


BODY_R = scad_num("body_r")
WELL_R = scad_num("well_r")
LEDGE_R = scad_num("ledge_r")
AP_D = scad_num("aperture_d")
APERTURES = scad_list("apertures")
SIGHT_D = scad_num("sight_d")
CODE_RING = scad_list("code_ring")
FRAG_RO, FRAG_RI, FRAG_GAP = scad_num("frag_ro"), scad_num("frag_ri"), scad_num("frag_gap")
FRAG_TEXT_R, FRAG_TEXT_H = scad_num("frag_text_r"), scad_num("frag_text_h")
COVER_R = scad_num("cover_r")
HUB_R, RING_CLEAR = scad_num("hub_r"), scad_num("ring_clear")
CAP_RI = scad_num("cap_ri")
SKIRT_RI = WELL_R - scad_num("cover_clear") - scad_num("skirt_wall")

# ---- clue-sheet layout ------------------------------------------------------
WORD = "TIME"                 # one letter per aperture, in `apertures` order
PITCH = 7.5                   # half-pitch of the diagonal letter lattice, mm: letters sit where
                              # i + j is even, so neighbours are 10.6 mm apart (apertures must
                              # sit on lattice points)
CAP_H = 5.0                   # capital height, mm
FONT = "Helvetica-Bold"
FONT_SIZE = CAP_H / 0.718     # Helvetica cap height = 0.718 em   (value in mm)
FIELD_R = 31.0                # letters fill this radius (well is 25 mm)
SEED = 1847

PAGE_W, PAGE_H = letter
CX, CY = PAGE_W / 2 / mm, PAGE_H / 2 / mm + 12   # device centre on the page, mm


def letter_field():
    """[(x, y, char)] in mm relative to the device centre."""
    rnd = random.Random(SEED)
    target = {tuple(p): ch for p, ch in zip(APERTURES, WORD)}
    for p in target:
        assert all(abs(c / PITCH - round(c / PITCH)) < 1e-6 for c in p) and \
            round(p[0] / PITCH + p[1] / PITCH) % 2 == 0, "aperture off the letter lattice"
    n = int(FIELD_R // PITCH) + 1
    cells = []
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            x, y = i * PITCH, j * PITCH
            if math.hypot(x, y) > FIELD_R or (i == 0 and j == 0) or (i + j) % 2:
                continue
            ch = target.get((x, y)) or rnd.choice("ABCDEFGHJKLMNOPRSTUVWXYZ")
            cells.append((x, y, ch))
    return cells


def glyph_box(x, y, ch):
    w = stringWidth(ch, FONT, FONT_SIZE)
    return (x - w / 2, y - CAP_H / 2, x + w / 2, y + CAP_H / 2)


def box_circle_relation(box, cx, cy, r):
    """'inside' if the box is fully in the circle, 'outside' if disjoint, else 'partial'."""
    x0, y0, x1, y1 = box
    far = max(math.hypot(px - cx, py - cy) for px in (x0, x1) for py in (y0, y1))
    nx, ny = min(max(cx, x0), x1), min(max(cy, y0), y1)
    near = math.hypot(nx - cx, ny - cy)
    return "inside" if far <= r else "outside" if near >= r else "partial"


def verify(cells, dx=0.0, dy=0.0):
    """Check what each aperture shows when the mask is misplaced by (dx, dy)."""
    ok = True
    for (ax, ay), want in zip(APERTURES, WORD):
        seen, clipped = [], []
        for x, y, ch in cells:
            rel = box_circle_relation(glyph_box(x, y, ch), ax + dx, ay + dy, AP_D / 2)
            if rel == "inside":
                seen.append(ch)
            elif rel == "partial":
                clipped.append(ch)
        if seen != [want] or clipped:
            ok = False
    return ok


def mm_line(c, x0, y0, x1, y1):
    c.line((CX + x0) * mm, (CY + y0) * mm, (CX + x1) * mm, (CY + y1) * mm)


def polar(r, a):
    return r * math.cos(math.radians(a)), r * math.sin(math.radians(a))


def aperture_sheet(cells):
    path = os.path.join(OUT, "aperture_test_sheet.pdf")
    c = canvas.Canvas(path, pagesize=letter)
    c.setTitle("Chronometer - aperture test sheet")
    c.setFont(FONT, FONT_SIZE * mm)
    for x, y, ch in cells:
        c.drawCentredString((CX + x) * mm, (CY + y - CAP_H / 2) * mm, ch)
    # centre target for the sighting hole
    c.setLineWidth(0.3 * mm)
    c.circle(CX * mm, CY * mm, 2.2 * mm)
    c.circle(CX * mm, CY * mm, 0.6 * mm, fill=1)
    # footprint + registration ticks (match the notches in the base rim)
    c.setStrokeGray(0.55)
    c.setLineWidth(0.25 * mm)
    c.circle(CX * mm, CY * mm, (BODY_R + 0.3) * mm)
    c.setStrokeGray(0)
    c.setLineWidth(0.4 * mm)
    for a in (0, 180, 270, 87, 93):
        mm_line(c, *polar(BODY_R - 2.5, a), *polar(BODY_R + 12, a))
    tx, ty = polar(BODY_R + 16, 90)
    p = c.beginPath()
    p.moveTo((CX + tx - 2.5) * mm, (CY + ty) * mm)
    p.lineTo((CX + tx + 2.5) * mm, (CY + ty) * mm)
    p.lineTo((CX + tx) * mm, (CY + ty - 3.5) * mm)
    p.close()
    c.drawPath(p, fill=1)
    c.setFont("Helvetica", 8)
    c.drawCentredString((CX + tx) * mm, (CY + ty + 1.5) * mm, "TOP - double notch")
    # scale check + instructions
    y0 = 18
    c.setLineWidth(0.3 * mm)
    c.line(30 * mm, y0 * mm, 130 * mm, y0 * mm)
    for i in range(11):
        c.line((30 + 10 * i) * mm, y0 * mm, (30 + 10 * i) * mm, (y0 + (3 if i % 5 == 0 else 1.5)) * mm)
    c.drawString(30 * mm, (y0 - 4) * mm, "Scale check: this bar must measure exactly 100 mm. Print at 100 % (\"Actual size\").")
    c.setFont("Helvetica", 9)
    for i, line in enumerate([
        "CHRONOMETER - TEMPORAL APERTURE TEST SHEET (prototype validation)",
        "1. Remove the centre cover (quarter-twist anticlockwise, lift).",
        "2. Set the instrument on the grey circle. Line up the four rim notches with the ticks; the double notch goes to TOP.",
        "3. Fine-tune until the centre target is visible through the small sighting hole.",
        "4. Read the four apertures clockwise from the top mark.   Expected: T - I - M - E",
    ]):
        c.drawString(20 * mm, (PAGE_H / mm - 14 - 4.6 * i) * mm, line)
    c.showPage()
    c.save()
    return path


# ---- labels / templates -----------------------------------------------------
def sym(c, name, s=3.2):
    """Draw a symbol centred at the origin inside a +/- s mm box."""
    c.setLineWidth(0.45 * mm)
    u = s * mm
    if name == "sun":
        c.circle(0, 0, 0.42 * u, fill=1)
        for k in range(8):
            a = math.radians(45 * k)
            c.line(0.62 * u * math.cos(a), 0.62 * u * math.sin(a), u * math.cos(a), u * math.sin(a))
    elif name == "moon":
        c.circle(0, 0, 0.85 * u, fill=1)
        c.setFillGray(1)
        c.circle(0.38 * u, 0.12 * u, 0.72 * u, fill=1, stroke=0)
        c.setFillGray(0)
    elif name == "star":
        p = c.beginPath()
        for k in range(10):
            r = u if k % 2 == 0 else 0.42 * u
            a = math.radians(90 + 36 * k)
            (p.moveTo if k == 0 else p.lineTo)(r * math.cos(a), r * math.sin(a))
        p.close()
        c.drawPath(p, fill=1)
    elif name == "hourglass":
        p = c.beginPath()
        p.moveTo(-0.7 * u, u); p.lineTo(0.7 * u, u); p.lineTo(-0.7 * u, -u); p.lineTo(0.7 * u, -u); p.close()
        c.drawPath(p, fill=1)
    elif name == "diamond":
        p = c.beginPath()
        p.moveTo(0, u); p.lineTo(0.65 * u, 0); p.lineTo(0, -u); p.lineTo(-0.65 * u, 0); p.close()
        c.drawPath(p, fill=1)
    elif name == "triangle":
        p = c.beginPath()
        p.moveTo(0, 0.9 * u); p.lineTo(0.85 * u, -0.7 * u); p.lineTo(-0.85 * u, -0.7 * u); p.close()
        c.drawPath(p, fill=0)
    elif name == "wave":
        for dy in (-0.35 * u, 0.35 * u):
            p = c.beginPath()
            p.moveTo(-u, dy)
            p.curveTo(-0.5 * u, dy + 0.6 * u, -0.5 * u, dy - 0.6 * u, 0, dy)
            p.curveTo(0.5 * u, dy + 0.6 * u, 0.5 * u, dy - 0.6 * u, u, dy)
            c.drawPath(p)
    elif name == "cross":
        c.setLineWidth(0.9 * mm)
        c.line(0, -u, 0, u); c.line(-0.7 * u, 0.3 * u, 0.7 * u, 0.3 * u)
    elif name == "eye":
        p = c.beginPath()
        p.moveTo(-u, 0); p.curveTo(-0.4 * u, 0.8 * u, 0.4 * u, 0.8 * u, u, 0)
        p.curveTo(0.4 * u, -0.8 * u, -0.4 * u, -0.8 * u, -u, 0)
        c.drawPath(p)
        c.circle(0, 0, 0.3 * u, fill=1)
    elif name == "square":
        c.rect(-0.7 * u, -0.7 * u, 1.4 * u, 1.4 * u, fill=0)
        c.circle(0, 0, 0.15 * u, fill=1)
    elif name == "ring":
        c.circle(0, 0, 0.8 * u)
        c.circle(0, 0, 0.4 * u)
    elif name == "arrow":
        c.setLineWidth(0.8 * mm)
        c.line(0, -u, 0, 0.8 * u); c.line(0, u, -0.6 * u, 0.2 * u); c.line(0, u, 0.6 * u, 0.2 * u)


# clock position -> symbol (demo dial). Position 0 is the "home" symbol.
SYMBOLS = ["sun", "moon", "triangle", "wave", "star", "cross", "eye", "hourglass", "square", "ring", "diamond", "arrow"]
DEMO_SEQUENCE = ["moon", "star", "hourglass", "diamond"]


def arc_path(c, cx, cy, ri, ro, a0, a1):
    p = c.beginPath()
    p.arc((cx - ro) * mm, (cy - ro) * mm, (cx + ro) * mm, (cy + ro) * mm, a0, a1 - a0)
    p.arcTo((cx - ri) * mm, (cy - ri) * mm, (cx + ri) * mm, (cy + ri) * mm, a1, a0 - a1)
    p.close()
    return p


def labels_sheet():
    path = os.path.join(OUT, "labels_and_templates.pdf")
    c = canvas.Canvas(path, pagesize=letter)
    c.setTitle("Chronometer - labels and templates")
    W, H = PAGE_W / mm, PAGE_H / mm
    lab_ri, lab_ro = HUB_R + RING_CLEAR + 1.2 + 0.3, CAP_RI - 0.3 - 1.2 - 0.3

    def heading(x, y, text, size=10):
        c.setFont("Helvetica-Bold", size)
        c.drawString(x * mm, y * mm, text)

    def note(x, y, lines, size=8):
        c.setFont("Helvetica", size)
        for i, line in enumerate(lines):
            c.drawString(x * mm, (y - 3.6 * i) * mm, line)

    def label_ring(cx, cy, with_symbols):
        c.setLineWidth(0.15 * mm)
        c.setStrokeGray(0.5)
        for k in range(12):
            a = 90 - 30 * k
            c.drawPath(arc_path(c, cx, cy, lab_ri, lab_ro, a - 12, a + 12))
        c.setStrokeGray(0)
        if with_symbols:
            for k, name in enumerate(SYMBOLS):
                a = 90 - 30 * k
                x, y = polar((lab_ri + lab_ro) / 2, a)
                c.saveState()
                c.translate((cx + x) * mm, (cy + y) * mm)
                c.rotate(a - 90)
                sym(c, name)
                c.restoreState()

    # --- page 1: ring labels + UV inserts
    heading(15, H - 15, "CHRONOMETER - inner-ring symbol labels (print on matte sticker paper, 100 %)")
    note(15, H - 20, ["Cut each sector on the grey line and stick it into a label pocket of the inner ring. The sun is the home symbol.",
                      "Left: demo dial.  Right: blank set for the real game."])
    label_ring(60, H - 72, True)
    label_ring(155, H - 72, False)
    c.setFont("Helvetica", 7)
    c.drawCentredString(60 * mm, (H - 73) * mm, "demo dial")
    c.drawCentredString(155 * mm, (H - 73) * mm, "blank")

    heading(15, H - 130, "UV insert discs (plain paper; write the hidden message with a UV-reactive pen)")
    note(15, H - 135, ["Cut on the outer circle, punch the centre hole, lay inside the centre cover (face out) and press the split ring in.",
                       "Keep the writing inside the dashed circle so the retaining ring does not hide it."])
    for i in range(3):
        cx, cy = 45 + 62 * i, H - 170
        c.setLineWidth(0.15 * mm)
        c.setStrokeGray(0.5)
        c.circle(cx * mm, cy * mm, (SKIRT_RI - 0.3) * mm)
        c.circle(cx * mm, cy * mm, 2.0 * mm)
        c.setDash(1.5, 1.5)
        c.circle(cx * mm, cy * mm, (SKIRT_RI - 2.2) * mm)
        c.setDash()
        c.setStrokeGray(0)

    y0 = 22
    c.setLineWidth(0.3 * mm)
    c.line(30 * mm, y0 * mm, 130 * mm, y0 * mm)
    for i in range(11):
        c.line((30 + 10 * i) * mm, y0 * mm, (30 + 10 * i) * mm, (y0 + (3 if i % 5 == 0 else 1.5)) * mm)
    note(30, y0 - 4, ["Scale check: this bar must measure exactly 100 mm."])
    c.showPage()

    # --- page 2: fragment template + demo decoding card
    heading(15, H - 15, "CHRONOMETER - fragment template and demo decoding (prototype validation)")
    cx, cy = 62, H - 68
    c.setLineWidth(0.2 * mm)
    c.setStrokeGray(0.5)
    c.circle(cx * mm, cy * mm, COVER_R * mm)
    c.setStrokeGray(0)
    half = math.degrees(math.asin(FRAG_GAP / 2 / FRAG_RO))
    for i in range(4):
        cen = 90 - 90 * i
        half_i = math.degrees(math.asin(FRAG_GAP / 2 / (FRAG_RI + 2.4)))
        p = c.beginPath()
        a0, a1 = cen - 45 + half, cen + 45 - half
        p.arc((cx - FRAG_RO) * mm, (cy - FRAG_RO) * mm, (cx + FRAG_RO) * mm, (cy + FRAG_RO) * mm, a0, a1 - a0)
        ri = FRAG_RI + 2.4
        p.arcTo((cx - ri) * mm, (cy - ri) * mm, (cx + ri) * mm, (cy + ri) * mm, cen + 45 - half_i, -(90 - 2 * half_i))
        p.close()
        c.drawPath(p)
        for j in (-1, 0, 1):
            k = (3 * i + j) % 12
            a = 90 - 30 * k
            x, y = polar(FRAG_TEXT_R, a)
            c.saveState()
            c.translate((cx + x) * mm, (cy + y) * mm)
            c.rotate(a - 90)
            c.setFont("Helvetica-Bold", FRAG_TEXT_H / 0.718 * mm)
            c.drawCentredString(0, -FRAG_TEXT_H / 2 * mm, CODE_RING[k])
            c.restoreState()
        x, y = polar(FRAG_RO + 6, cen)
        c.setFont("Helvetica", 8)
        c.drawCentredString((cx + x) * mm, (cy + y - 1) * mm, "fragment %d" % (i + 1))
    c.circle(cx * mm, cy * mm, 10 * mm)
    c.setFont("Helvetica", 6)
    c.drawCentredString(cx * mm, (cy - 1) * mm, "keystone")
    c.setFont("Helvetica", 8)
    c.drawCentredString(cx * mm, (cy - 46) * mm, "1 : 1 top view, fragments seated on the centre cover (XII at top)")

    x = 118
    heading(x, H - 30, "Demo final instruction (code 1847)")
    seq = DEMO_SEQUENCE
    code = "".join(CODE_RING[SYMBOLS.index(s)] for s in seq)
    note(x, H - 36, [
        "1. Seat the four fragments on the centre cover (the pegs only",
        "    fit one socket each) and screw the keystone down.",
        "2. Turn the inner ring until the SUN stands at the index mark.",
        "3. Each symbol now points at one character on the fragments.",
        "    Read them in this order:",
    ])
    for i, s in enumerate(seq):
        c.saveState()
        c.translate((x + 8 + 20 * i) * mm, (H - 64) * mm)
        sym(c, s)
        c.restoreState()
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString((x + 8 + 20 * i) * mm, (H - 74) * mm, code[i])
        c.setFont("Helvetica", 7)
        c.drawCentredString((x + 8 + 20 * i) * mm, (H - 78) * mm, s)
    note(x, H - 86, ["Result: %s.  With the ring one click off, the same symbols" % code,
                     "read %s - the alignment matters." % "".join(
                         CODE_RING[(SYMBOLS.index(s) + 1) % 12] for s in seq)])

    heading(15, H - 135, "Code ring (clockwise from XII)")
    c.setFont("Courier-Bold", 11)
    c.drawString(15 * mm, (H - 142) * mm, "  ".join("%s:%s" % (r, ch) for r, ch in zip(
        ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"], CODE_RING)))
    note(15, H - 149, [
        "Fragment 1 carries XI-XII-I, fragment 2 II-III-IV, fragment 3 V-VI-VII, fragment 4 VIII-IX-X.",
        "To change the final code, edit `code_ring` in cad/chronometer.scad and re-export the four fragments -",
        "or keep the fragments and change which symbols / which home position the final clue names.",
    ])
    assert code == "1847", code
    c.showPage()
    c.save()
    return path


def proof(pdf_path):
    """Rasterise the sheet and lay a mask over it - what the player sees through the well."""
    from PIL import Image, ImageDraw
    dpi = 200
    base = os.path.join(OUT, "_tmp_sheet")
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", "-singlefile", pdf_path, base], check=True)
    page = Image.open(base + ".png").convert("RGB")
    os.remove(base + ".png")
    s = dpi / 25.4

    def px(x, y):
        return ((CX + x) * s, page.size[1] - (CY + y) * s)

    def view(dx, dy, caption):
        """Mask as a separate layer: opaque brass body, black stencil, holes cut through."""
        layer = Image.new("RGBA", page.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)

        def disc(x, y, r, fill):
            cx, cy = px(x + dx, y + dy)
            d.ellipse([cx - r * s, cy - r * s, cx + r * s, cy + r * s], fill=fill)

        disc(0, 0, BODY_R, (150, 120, 60, 255))
        disc(0, 0, WELL_R, (25, 25, 28, 255))
        for ax, ay in APERTURES:
            disc(ax, ay, AP_D / 2, (0, 0, 0, 0))
        if SIGHT_D:
            disc(0, 0, SIGHT_D / 2, (0, 0, 0, 0))
        out = Image.alpha_composite(page.convert("RGBA"), layer).convert("RGB")
        cx, cy = px(dx, dy)
        r = 34 * s
        crop = out.crop([int(cx - r), int(cy - r), int(cx + r), int(cy + r)])
        ImageDraw.Draw(crop).text((10, 8), caption, fill=(255, 255, 255))
        return crop

    r = 34 * s
    cx, cy = px(0, 0)
    bare = page.crop([int(cx - r), int(cy - r), int(cx + r), int(cy + r)])
    ImageDraw.Draw(bare).text((10, 8), "sheet without the instrument", fill=(0, 0, 0))
    tiles = [bare, view(0, 0, "mask registered"), view(1.0, -1.0, "mask misplaced 1 mm right, 1 mm down")]
    w, h = tiles[0].size
    out = Image.new("RGB", (w * 3 + 40, h), "white")
    for i, t in enumerate(tiles):
        out.paste(t, (i * (w + 20), 0))
    out.save(os.path.join(OUT, "aperture_proof.png"))


if __name__ == "__main__":
    cells = letter_field()
    assert verify(cells), "registered mask does not read the word cleanly"
    tol = 0.0
    while tol < 3 and all(verify(cells, tol * math.cos(a), tol * math.sin(a))
                          for a in [i * math.pi / 8 for i in range(16)]):
        tol += 0.05
    print("Aperture check: reads %s when registered; still clean (whole letter visible, no neighbour "
          "intruding) for placement errors up to %.2f mm in any direction" % (WORD, tol - 0.05))
    pdf = aperture_sheet(cells)
    labels_sheet()
    proof(pdf)
    print("wrote", ", ".join(sorted(os.listdir(OUT))))
