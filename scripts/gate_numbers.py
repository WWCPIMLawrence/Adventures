#!/usr/bin/env python3
"""Hand-calculation of the push-and-turn gate: bow spring stiffness and strain, press force, knob torque margin.
Beam theory only. Nothing here is a measurement."""
import math
# --- geometry (cad/chronometer.scad defaults) ---
c, w, lift = 14.0, 1.4, 1.2          # chord, radial width, free lift (= arch sag)
n_bows = 6
r_lug = 25.3                          # mean radius of a lug/pocket wall
gate_h, track0 = 0.9, 0.54            # pocket step; ceiling lift beside the pocket (nominal)
print("BOW SPRINGS (6 per instrument, simply-supported arch, frictionless ends = lower bound on stiffness)")
print(f"{'material':10s}{'t mm':>6s}{'k/bow N/mm':>12s}{'k x6 N/mm':>11s}{'strain %':>10s}{'F rest N':>10s}{'F full N':>10s}")
for mat, E in (("PETG", 1900.0), ("PLA", 3300.0)):
    for t in (0.6, 0.7, 0.8, 0.9):
        I = w * t**3 / 12
        k = 48 * E * I / c**3
        kappa = 8 * lift / c**2
        eps = kappa * t / 2 * 100
        # cover floats against the pocket ceiling at (track0 + gate_h) minus ~0.4 print droop = real lift
        f_full = n_bows * k * lift
        print(f"{mat:10s}{t:6.1f}{k:12.2f}{n_bows*k:11.1f}{eps:10.2f}{'':>10s}{f_full:10.1f}")
print()
print("PRESS FORCE TO UNLOCK (cover must come down from the pocket height to the track height)")
for t, E in ((0.7, 1900.0), (0.8, 1900.0)):
    k = 48 * E * (w * t**3 / 12) / c**3 * n_bows
    for pocket_lift in (1.2, 1.0):   # 1.0 = pocket ceiling lowered by print droop
        stroke_to_clear = pocket_lift - 0.15   # real track ceiling is ~0.1-0.2 above the hub after droop
        print(f"  t={t} mm, cover floating at {pocket_lift:.1f} mm: press {k*(lift-(lift-stroke_to_clear)):.1f}..{k*(lift-0.0):.1f} N "
              f"(to clear the wall .. to the hub) - the cover must travel {stroke_to_clear:.2f} mm")
print()
print("TORQUE MARGIN: wall contact vs what a hand can put into the knob")
for torque in (200, 500, 1000):  # N mm
    F = torque / r_lug / 3
    area = gate_h * 1.4          # mm^2, wall height above the track ceiling x radial depth of the lug
    print(f"  knob torque {torque:5d} N mm -> {F:5.1f} N per lug on {area:.1f} mm^2 = {F/area:5.1f} MPa (PLA shear/bearing ~ 20-40 MPa along layers)")
print()
print("WHAT THE OLD LATCH HELD (for comparison): 3 nubs, ~1 N each at 45 deg flank, r 25 -> ~", round(3*1.0*25), "N mm, falling with creep")
print("Friction drag of the sprung cover on the track ceiling while turning: mu 0.3 x 9 N x r 25 =", round(0.3*9*25), "N mm (what a player feels when turning)")
