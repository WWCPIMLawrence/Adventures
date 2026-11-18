#!/usr/bin/env python3
"""NON-PRODUCTION. 1:1 paper test overlay for the M-72 attachment concept: cut lines and punch marks, same geometry as m72_sight_plate_concept.scad."""
import math
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
screw_r, screw_angles, head_hole = 45.0, [25, 150, 270], 6.4
win_p = [4, 6, 8]; win_w = 12
W, H = letter; cx, cy = W/2, H/2 + 4*mm
c = canvas.Canvas("m72_paper_overlay_template_NONPRODUCTION.pdf", pagesize=letter)
c.setTitle("M-72 attachment: paper test overlay (non-production concept), 1:1")
P = lambda x, y: (cx + x*mm, cy + y*mm)
c.setFont("Helvetica-Bold", 11); c.drawString(15*mm, H - 12*mm, "M-72 calibration attachment: PAPER TEST OVERLAY (concept, not production)")
c.setFont("Helvetica", 8)
c.drawString(15*mm, H - 17*mm, "Print at 100 % on cardstock (check the 100 mm bar). Cut on the SOLID lines (outer circle, inner circle, all windows). Punch or cut the three")
c.drawString(15*mm, H - 21*mm, "round holes over the screw heads (6.4 mm). Lay it on the instrument: the three holes drop over the three black cap-screw heads; it fits one way only.")
c.drawString(15*mm, H - 25*mm, "View from above, double notch / fixed arrow at the top. Windows are at clock positions 4, 6 and 8 clockwise of the fixed arrow (A, B, C).")
c.setLineWidth(0.6)
c.circle(cx, cy, 62*mm); c.circle(cx, cy, 29*mm)                                   # cut lines
def rect_polar(ang, r0, r1, w):                                                    # radial rectangle at CAD angle ang
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); vx, vy = -uy, ux
    pts = [(r0*ux - w/2*vx, r0*uy - w/2*vy), (r1*ux - w/2*vx, r1*uy - w/2*vy), (r1*ux + w/2*vx, r1*uy + w/2*vy), (r0*ux + w/2*vx, r0*uy + w/2*vy)]
    p = c.beginPath(); p.moveTo(*P(*pts[0]))
    for q in pts[1:]: p.lineTo(*P(*q))
    p.close(); c.drawPath(p, stroke=1, fill=0)
for i, pos in enumerate(win_p):
    ang = 90 - 30*pos
    rect_polar(ang, 30.2, 38.8, win_w); rect_polar(ang, 50.8, 59.8, win_w)
    lx, ly = P(40.4*math.cos(math.radians(ang)), 40.4*math.sin(math.radians(ang)))
    c.setFont("Helvetica-Bold", 8); c.drawCentredString(lx, ly - 1.0*mm, "ABC"[i])
rect_polar(90, 40.6, 49.6, 9)                                                      # window over the fixed arrow on the index cap
c.setLineWidth(0.4); c.setDash(1.5, 1.5)
for a in screw_angles:                                                              # punch marks
    x, y = P(screw_r*math.cos(math.radians(a)), screw_r*math.sin(math.radians(a))); c.circle(x, y, head_hole/2*mm)
c.setDash()
c.setFont("Helvetica", 6.5); c.drawString(cx + 1.5*mm, cy + 51*mm, "ARROW window"); 
c.setFont("Helvetica", 6.5)
for a in screw_angles:
    x, y = P(screw_r*math.cos(math.radians(a)), screw_r*math.sin(math.radians(a))); c.drawString(x + 4*mm, y - 1*mm, "punch")
y0 = 22*mm; c.setLineWidth(0.6); c.line(15*mm, y0, 115*mm, y0)
for k in range(0, 101, 10): c.line((15+k)*mm, y0, (15+k)*mm, y0 + (3 if k % 50 == 0 else 1.8)*mm)
c.setFont("Helvetica", 7); c.drawString(15*mm, y0 - 4*mm, "SCALE CHECK: this bar must measure exactly 100 mm.")
c.drawString(15*mm, 11*mm, "Concept only. Geometry: concepts/m72_attachment/m72_sight_plate_concept.scad. Heads: M3 socket, 5.5 mm, at r 45 mm, CAD angles 25, 150, 270 deg.")
c.showPage(); c.save(); print("ok")
