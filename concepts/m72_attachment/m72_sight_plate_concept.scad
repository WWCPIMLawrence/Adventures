// NON-PRODUCTION CONCEPT for the M-72 removable calibration attachment ("sight plate").
// It includes the real Chronometer CAD only to test fit. Nothing here changes, replaces or is read by the approved design.
include <../../cad/chronometer.scad>

plate_t = 2.0;        // plate thickness: must exceed cup_depth, or the cups become through-holes and the heads cannot hold the plate up
cup_d = 6.3;          // locating cup over each cap-screw head (head is 5.5): +/-0.4 mm
cup_depth = 1.2;      // blind cup depth (0.8 mm roof above it): the heads stop the plate here, its underside 0.8 mm above the tallest ring feature (ribs, 6.4)
plate_ri = 28.6;      // just inside the inner ring's face (28.3 starts) and 0.8 mm clear of the cover (27.8)
plate_ro = 62.0;      // inside the outer ring's edge (62.5)
win_p = [4, 6, 8];    // sketch only: clock positions (clockwise of the fixed arrow) of three window PAIRS
// Window sizes come from the measured glyphs (widest numeral VIII 12.6 x 8.2 mm; symbols up to 7.1 x 7.0 mm) plus a registration budget:
numeral_win = [50.3, 60.9, 16.0];   // radial r0, r1 and tangential width (numerals centre at r 55.6)
symbol_win  = [29.6, 38.9, 10.0];   // (symbols centre at r 34.0)
cham = 1.0;                         // 45 deg chamfer on the top edge of every window: recovers most of the parallax loss

head_top = z_cap + cap_t + 3;                 // top of the cap-screw heads, in assembly height
plate_z0 = head_top - cup_depth;              // underside of the plate

module win_cut(r0, r1, w) {       // radial rectangle, straight wall, chamfered on top (local frame: radial = +x, tangential = y)
  translate([0, 0, -1]) linear_extrude(plate_t - cham + 1.01) translate([r0, -w/2]) square([r1 - r0, w]);
  hull() {
    translate([0, 0, plate_t - cham]) linear_extrude(0.01) translate([r0, -w/2]) square([r1 - r0, w]);
    translate([0, 0, plate_t]) linear_extrude(0.01) translate([r0 - cham, -w/2 - cham]) square([r1 - r0 + 2*cham, w + 2*cham]);
  }
}
module window_pair(p) rotate([0, 0, 90 - 30*p]) { win_cut(symbol_win[0], symbol_win[1], symbol_win[2]); win_cut(numeral_win[0], numeral_win[1], numeral_win[2]); }
module arrow_window() rotate([0, 0, 90]) translate([40.6, -4.5]) square([9.0, 9.0]);   // keeps the fixed arrow on the index cap visible
module sight_plate(dz = 0) translate([0, 0, plate_z0 + dz]) difference() {
  linear_extrude(plate_t) difference() {
    difference() { circle(r = plate_ro, $fn = 160); circle(r = plate_ri, $fn = 160); }
    arrow_window();
  }
  for (p = win_p) window_pair(p);
  for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, -1]) cylinder(d = cup_d, h = cup_depth + 1, $fn = 32);
}
module heads_at_assembly() for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, head_top - 3]) cylinder(d = 5.5, h = 3, $fn = 24);

// ---- exports and fit checks (run with -D part="..."; the approved defaults are used unchanged) ----
if (part == "m72_plate") sight_plate();
if (part == "m72_plate_print") translate([0, 0, -plate_z0]) sight_plate();            // flat on the bed, underside down (cups are holes from the bed: no overhang)
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
