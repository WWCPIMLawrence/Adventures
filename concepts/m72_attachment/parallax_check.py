#!/usr/bin/env python3
"""NON-PRODUCTION. How much of a glyph can a player see through a window at ordinary viewing angles?
Geometry (above the deck floor, from cad/chronometer.scad): ring faces 5.6; raised numerals and symbols top out at 6.0.
Rigid plate: underside 7.2, top 9.2 (2.0 thick). Paper: lies on the ribs (6.4), 0.2 thick.
A glyph point P is visible if the sight line from P toward the eye passes through the window at the plate's underside AND at its top."""
import math
def visible_fraction(win, glyph, z_g, z_bot, z_top, theta_deg, phi_deg, off, bevel=0.0):
    wx, wy = win; gx, gy = glyph; ox, oy = off                 # window size, glyph size, glyph offset from the window centre (registration + ring error)
    t = math.tan(math.radians(theta_deg)); dx, dy = t*math.cos(math.radians(phi_deg)), t*math.sin(math.radians(phi_deg))
    z2 = z_bot + (z_top - z_bot - bevel) if bevel else z_top   # a 45 deg chamfer on the top edge leaves a straight wall of (thickness - bevel)
    n = 0; tot = 0
    for i in range(41):
        for j in range(41):
            px = ox - gx/2 + gx*i/40; py = oy - gy/2 + gy*j/40
            ok = True
            for z in (z_bot, z2):
                x = px + (z - z_g)*dx; y = py + (z - z_g)*dy
                if abs(x) > wx/2 or abs(y) > wy/2: ok = False
            n += ok; tot += 1
    return n/tot
cases = {                                     # window (tangential x radial), glyph, registration offset (tangential, radial) = plate seating + ring detent error
  "numeral VIII, window 16.0 x 10.6": ((16.0, 10.6), (12.6, 8.2), (1.2, 0.9)),
  "numeral VIII, OLD window 12.0 x 9.0": ((12.0, 9.0), (12.6, 8.2), (0.0, 0.0)),
  "symbol (7.1 x 7.0), window 10.0 x 9.3": ((10.0, 9.3), (7.1, 7.0), (0.9, 0.9)),
}
def worst(case, z_g, zb, zt, theta, bevel=0.0):
    win, gl, (ex, ey) = cases[case]
    return min(visible_fraction(win, gl, z_g, zb, zt, theta, phi, (sx*ex, sy*ey), bevel) for phi in range(0, 360, 15) for sx in (-1, 1) for sy in (-1, 1))
print("worst-case visible fraction of the glyph (over every viewing direction and every registration-error corner)\n")
for label, (zb, zt, bevel) in {"rigid plate 2.0 mm, square window edges": (7.2, 9.2, 0.0), "rigid plate 2.0 mm, 1.0 mm 45 deg chamfer on top": (7.2, 9.2, 1.0), "paper overlay on the ribs": (6.4, 6.6, 0.0)}.items():
    print(label)
    for case in cases:
        print(f"  {case:40s}", "  ".join(f"{th:2d} deg: {100*worst(case, 6.0, zb, zt, th, bevel):3.0f} %" for th in (0, 15, 25, 35, 45)))
    print()
