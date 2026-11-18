// NON-PRODUCTION CONCEPT for the M-72 removable calibration attachment ("sight plate").
// It includes the real Chronometer CAD only to test fit. Nothing here changes, replaces or is read by the approved design.
include <../../cad/chronometer.scad>

plate_t = 2.0;        // plate thickness: must exceed cup_depth, or the cups become through-holes and the heads cannot hold the plate up
cup_d = 6.3;          // locating cup over each cap-screw head (head is 5.5): +/-0.4 mm
cup_depth = 1.2;      // blind cup depth (0.8 mm roof above it): the heads stop the plate here, its underside 0.8 mm above the tallest ring feature (ribs, 6.4)
plate_ri = 29.0;      // inside the inner ring's face (28.3) and clear of the cover (27.8)
plate_ro = 62.0;      // inside the outer ring's edge (62.5)
win_p = [4, 6, 8];    // sketch only: clock positions (clockwise of the fixed arrow) of three window PAIRS
win_w = 12;           // window width: shows one symbol and one numeral, hides the neighbours (30 deg pitch is 15.7 mm at r 30)

head_top = z_cap + cap_t + 3;                 // top of the cap-screw heads, in assembly height
plate_z0 = head_top - cup_depth;              // underside of the plate

module window_pair(p) rotate([0, 0, 90 - 30*p]) {
  translate([30.2, -win_w/2]) square([8.6, win_w]);      // over the inner ring's symbol band (symbols span r 30.5 to 37.5)
  translate([50.8, -win_w/2]) square([9.0, win_w]);      // over the outer ring's numeral band (numerals span r 52.1 to 59.1)
}                                                        // the solid web between them (r 38.8 to 50.8) carries the cups and a label
module arrow_window() rotate([0, 0, 90]) translate([40.6, -4.5]) square([9.0, 9.0]);   // keeps the fixed arrow on the index cap visible
module sight_plate(dz = 0) translate([0, 0, plate_z0 + dz]) difference() {
  linear_extrude(plate_t) difference() {
    difference() { circle(r = plate_ro, $fn = 160); circle(r = plate_ri, $fn = 160); }
    for (p = win_p) window_pair(p);
    arrow_window();
  }
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
