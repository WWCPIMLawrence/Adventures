#!/usr/bin/env python3
"""reference/aperture_template_asym_v1.pdf - 1:1 engineering reference for the asymmetric aperture proposal (not game artwork)."""
import json, math, os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
doc = json.load(open(os.path.join(ROOT, "reference", "aperture_geometry.json")))
OUT = os.path.join(ROOT, "reference", "aperture_template_asym_v1.pdf")
W, H = letter
c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle("Chronometer aperture template asym_v1 (1:1, engineering reference)")
cx, cy = W / 2, H - 38 * mm - 62.5 * mm - 10 * mm   # centre of the instrument on the page


def P(x, y):  # CAD top view mm -> page points
    return cx + x * mm, cy + y * mm


c.setFont("Helvetica-Bold", 12)
c.drawString(15 * mm, H - 14 * mm, "Chronometer aperture template  asym_v1   -  ENGINEERING REFERENCE, PROPOSAL ONLY")
c.setFont("Helvetica", 8)
c.drawString(15 * mm, H - 19 * mm, "Print at 100 % (no fit-to-page) and check the scale bar. View: looking DOWN onto the instrument; a face-up sheet is drawn in this same view. NO mirror.")
c.drawString(15 * mm, H - 23 * mm, "Reading order: from the DOUBLE notch (12 o'clock) sweep CLOCKWISE: R, I, F, T.")
c.drawString(15 * mm, H - 27 * mm, "Not game artwork. The final sheet is made from reference/aperture_geometry.json.")
# instrument outline, well, coupon circle
c.setLineWidth(0.4); c.setStrokeGray(0.0)
c.circle(cx, cy, 62.5 * mm); c.setDash(2, 2); c.circle(cx, cy, 25 * mm); c.circle(cx, cy, 34 * mm); c.setDash()
c.setFont("Helvetica", 6); c.drawString(cx + 25.5 * mm * math.cos(math.radians(-50)), cy + 25.5 * mm * math.sin(math.radians(-50)), "well r 25")
c.drawString(cx + 34.5 * mm * math.cos(math.radians(-60)), cy + 34.5 * mm * math.sin(math.radians(-60)), "coupon r 34")
# axes
c.setStrokeGray(0.5); c.setLineWidth(0.2)
c.line(cx - 70 * mm, cy, cx + 70 * mm, cy); c.line(cx, cy - 70 * mm, cx, cy + 70 * mm); c.setStrokeGray(0)
# notches (CAD angles measured counter-clockwise from +X): singles 0, 180, 270; double 87 and 93
for a in (0, 180, 270, 87, 93):
    x, y = P(62.5 * math.cos(math.radians(a)), 62.5 * math.sin(math.radians(a)))
    c.setLineWidth(0.8)
    c.line(x - 4 * mm * math.cos(math.radians(a)), y - 4 * mm * math.sin(math.radians(a)), x + 4 * mm * math.cos(math.radians(a)), y + 4 * mm * math.sin(math.radians(a)))
    # coupon-edge mark at r 34
    x2, y2 = P(34 * math.cos(math.radians(a)), 34 * math.sin(math.radians(a)))
    c.line(x2 - 2.5 * mm * math.cos(math.radians(a)), y2 - 2.5 * mm * math.sin(math.radians(a)), x2 + 2.5 * mm * math.cos(math.radians(a)), y2 + 2.5 * mm * math.sin(math.radians(a)))
c.setFont("Helvetica-Bold", 7)
c.drawCentredString(cx, cy + 62.5 * mm + 6 * mm, "TOP: double notch (12 o'clock)")
c.setFont("Helvetica", 7)
c.drawString(cx + 62.5 * mm + 5 * mm, cy - 1 * mm, "single"); c.drawRightString(cx - 62.5 * mm - 5 * mm, cy - 1 * mm, "single"); c.drawCentredString(cx, cy - 62.5 * mm - 7 * mm, "single")
# sighting hole and centre mark
c.setLineWidth(0.4); c.circle(cx, cy, 1.25 * mm)
# holes
for h in doc["holes"]:
    x, y = P(h["x_mm"], h["y_mm"])
    c.setLineWidth(0.5); c.circle(x, y, 5.25 * mm)
    c.setStrokeGray(0.4); c.line(x - 7 * mm, y, x + 7 * mm, y); c.line(x, y - 7 * mm, x, y + 7 * mm); c.setStrokeGray(0)
    c.setFont("Helvetica-Bold", 16); c.drawCentredString(x, y - 2 * mm, h["letter"])
    c.setFont("Helvetica", 6); c.drawCentredString(x, y - 9 * mm, f"{h['order']}: ({h['x_mm']:.3f}, {h['y_mm']:.3f})")
# clockwise arrow from 12 o'clock
c.setLineWidth(0.5); c.setStrokeGray(0.25)
r = 21 * mm; pts = [(cx + r * math.sin(math.radians(b)), cy + r * math.cos(math.radians(b))) for b in range(4, 330, 6)]
for i in range(len(pts) - 1): c.line(*pts[i], *pts[i + 1])
c.setStrokeGray(0); c.setFont("Helvetica", 6); c.drawString(cx + 1.5 * mm, cy + 22.5 * mm, "start 12 o'clock, clockwise")
# scale bar
y0 = 62 * mm
c.setLineWidth(0.6); c.line(15 * mm, y0, 115 * mm, y0)
for k in range(0, 101, 10):
    c.line((15 + k) * mm, y0, (15 + k) * mm, y0 + (3 if k % 50 == 0 else 1.8) * mm)
c.setFont("Helvetica", 7); c.drawString(15 * mm, y0 - 4 * mm, "SCALE CHECK: this bar must measure exactly 100 mm (ticks every 10 mm)")
# table
c.setFont("Helvetica-Bold", 8); c.drawString(15 * mm, y0 - 10 * mm, "Hole centres (mm, from the plate centre; +X right, +Y toward the double notch)")
c.setFont("Helvetica", 8)
yy = y0 - 15 * mm
for h in doc["holes"]:
    c.drawString(15 * mm, yy, f"{h['order']}  {h['letter']}   x {h['x_mm']:+8.3f}   y {h['y_mm']:+8.3f}   (bearing {h['bearing_deg_clockwise_from_12_oclock']} deg, r {h['radius_mm']})   dia 10.5")
    yy -= 4 * mm
c.drawString(15 * mm, yy, "S  sighting hole   x +0.000   y +0.000   dia 2.5"); yy -= 4 * mm
c.setFont("Helvetica", 7); c.drawString(15 * mm, 14 * mm, "Floor 1.2 mm, flush (0 mm gap). Rim notches: singles 3, 6, 9 o'clock; double 12 o'clock (CAD 87/93 deg). Plate pin at 3 o'clock, r 54.")
c.drawString(15 * mm, 10 * mm, "Do not approximate, mirror, scale, rotate or reorder without engineering approval.   Version: asym_v1")
c.showPage(); c.save(); print("ok", OUT)
