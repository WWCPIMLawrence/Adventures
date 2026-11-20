// NON-PRODUCTION CONCEPT for the M-72 removable calibration attachment ("sight plate").
// It includes the real Chronometer CAD only to test fit. Nothing here changes, replaces or is read by the approved design.
include <../../cad/chronometer.scad>

head_d = 4.6;         // MEASURED by the owner, 20 Nov: pan-head cap screw head 4.6 mm wide x 1.9 mm tall
head_h = 1.9;
cup_d = head_d + 0.6; // locating cup in a boss under the plate: 0.3 mm radial clearance to the 4.6 mm head (the dome narrows towards its crown)
cup_depth = 1.4;      // cup is 1.4 deep: the roof touches only the dome's crown and the boss bottom stays 0.5 above the index cap's top face
boss_d = cup_d + 2.4; // boss around each cup, hangs below the plate body
body_clear = 0.8;     // plate body underside sits this far above the tallest ring feature (finger ribs, 6.4 above the ring floor)
plate_t = 2.0;        // plate body thickness
plate_ri = 28.6;      // just inside the inner ring's face (28.3 starts) and 0.8 mm clear of the cover (27.8)
plate_ro = 62.0;      // inside the outer ring's edge (62.5)
win_p = [4, 8, 10];    // sketch only: clock positions (clockwise of the fixed arrow) of three window PAIRS
// Window sizes come from the measured glyphs (widest numeral VIII 12.6 x 8.2 mm; symbols up to 7.1 x 7.0 mm) plus a registration budget:
numeral_win = [50.3, 60.9, 16.0];   // radial r0, r1 and tangential width (numerals centre at r 55.6)
symbol_win  = [29.6, 38.9, 10.0];   // (symbols centre at r 34.0)
cham = 1.0;                         // 45 deg chamfer on the top edge of every window: recovers most of the parallax loss

head_top = z_cap + cap_t + head_h;                 // top of the cap-screw heads, in assembly height
plate_z0 = z_floor + 6.4 + body_clear;       // underside of the plate BODY; the three bosses hang below it
boss_z0 = head_top - cup_depth;               // underside of the bosses (above the cap top by head_h - cup_depth)

// chamfer on the sides and on ONE radial end only: the symbol window keeps a straight inner wall and the numeral window a straight outer wall,
// because a chamfer there would run into the plate's edge (the old symmetric chamfer left a 0 to 0.1 mm sliver).
module win_cut(r0, r1, w, ch_in = 1, ch_out = 1) {   // radial rectangle (local frame: radial = +x, tangential = y)
  translate([0, 0, -1]) linear_extrude(plate_t - cham + 1.01) translate([r0, -w/2]) square([r1 - r0, w]);
  hull() {
    translate([0, 0, plate_t - cham]) linear_extrude(0.01) translate([r0, -w/2]) square([r1 - r0, w]);
    translate([0, 0, plate_t]) linear_extrude(0.01) translate([r0 - cham*ch_in, -w/2 - cham]) square([r1 - r0 + cham*(ch_in + ch_out), w + 2*cham]);
  }
}
module window_pair(p) rotate([0, 0, 90 - 30*p]) { win_cut(symbol_win[0], symbol_win[1], symbol_win[2], 0, 1); win_cut(numeral_win[0], numeral_win[1], numeral_win[2], 1, 0); }
module arrow_window() rotate([0, 0, 90]) translate([40.6, -4.5]) square([9.0, 9.0]);   // keeps the fixed arrow on the index cap visible
module sight_plate(dz = 0) translate([0, 0, dz]) difference() {
  union() {
    translate([0, 0, plate_z0]) linear_extrude(plate_t) difference() {
      difference() { circle(r = plate_ro, $fn = 160); circle(r = plate_ri, $fn = 160); }
      arrow_window();
    }
    for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, boss_z0]) cylinder(d = boss_d, h = plate_z0 - boss_z0 + 0.5, $fn = 48);
  }
  translate([0, 0, plate_z0]) for (p = win_p) window_pair(p);
  for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, boss_z0 - 1]) cylinder(d = cup_d, h = cup_depth + 1, $fn = 36);
}
module heads_at_assembly() for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, head_top - head_h]) cylinder(d = head_d, h = head_h, $fn = 24);

// ---- exports and fit checks (run with -D part="..."; the approved defaults are used unchanged) ----
if (part == "m72_plate") sight_plate();
if (part == "m72_plate_print") rotate([180, 0, 0]) translate([0, 0, -(plate_z0 + plate_t)]) sight_plate();   // print TOP FACE DOWN: smooth finished face on the bed, bosses and cups face up, no supports
// the plate must clear every existing part (EMPTY); the heads may only touch the cup ceilings
if (part == "chk_m72_rings") intersection() { sight_plate(); translate([0, 0, z_floor]) { outer_ring(); inner_ring(); } }
if (part == "chk_m72_cap") intersection() { sight_plate(); translate([0, 0, z_cap]) index_cap(); }
if (part == "chk_m72_heads") intersection() { sight_plate(); heads_at_assembly(); }
// support proof: sink the plate 0.1 mm and the heads MUST hit the cup roofs (SOLID); it must still be clear of the ribs and cap by then (EMPTY)
if (part == "chk_m72_stops") intersection() { sight_plate(-0.1); heads_at_assembly(); }
if (part == "chk_m72_sunk_clear") union() { intersection() { sight_plate(-0.1); translate([0, 0, z_floor]) { outer_ring(); inner_ring(); } } intersection() { sight_plate(-0.1); translate([0, 0, z_cap]) index_cap(); } }
if (part == "chk_m72_cover") union() { intersection() { sight_plate(); translate([0, 0, z_cap]) cover(); } intersection() { sight_plate(); translate([0, 0, z_cap + 1.2]) cover(); } }
// pictures
if (part == "m72_view") { assembly(fragments = true); color("#d94b3d") sight_plate(); }

// picture of a ring state: inner_rot / outer_rot in degrees (positive = anticlockwise). Correct calibration = outer 0 (XII at the arrow), inner +120 (STAR at the arrow).
inner_rot = 120; outer_rot = 0;
if (part == "m72_state") {
  translate([0, 0, z_floor]) { color("#2b2d33") rotate([0, 0, outer_rot]) outer_ring_body(); color("#e0d9c4") rotate([0, 0, outer_rot]) outer_ring_lettering();
                               color("#2b2d33") rotate([0, 0, inner_rot]) inner_ring_body(); color("#e0d9c4") rotate([0, 0, inner_rot]) inner_ring_lettering(); }
  translate([0, 0, z_cap]) { color("#c9a24a") index_cap_body(); color("#e0d9c4") index_cap_lettering(); }
  color("#d94b3d") sight_plate();
}
