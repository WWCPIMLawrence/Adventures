// M-72 SURVEYOR'S PLATE "V2r" = RAISED-DETAIL FEASIBILITY STUDY (Keeper request 21 Nov). PREVIEW / ANALYSIS ONLY: no STL is released.
// Same brass plate BODY as V1/V2b/V2c, but the top face stays FLAT (no engraving) and the black lettering and rings stand ABOVE it.
// Lettering/ring geometry is V2c's (grown glyphs, 0.8 mm rings); raised features are kept off the window chamfers.
include <m72_sight_plate_V2c.scad>

h_text = 0.4;      // raised height of the lettering and rule arcs (try 0.4 or 0.6; multiples of the 0.2 mm layer)
h_ring = 0.4;      // raised height of the concentric rings (0.3-0.4 requested; 0.4 = two layers; 0.2 = one layer)
keep_off = 0.3;    // raised features stay this far from every window's top (chamfered) opening
function topz() = plate_z0 + plate_t;
module win_top_fp(r0, r1, w, ch_in, ch_out) translate([r0 - cham*ch_in, -w/2 - cham]) square([r1 - r0 + cham*(ch_in + ch_out), w + 2*cham]);
module window_tops_2d() {
  for (p = win_p) rotate([0, 0, 90 - 30*p]) { win_top_fp(symbol_win[0], symbol_win[1], symbol_win[2], 0, 1); win_top_fp(numeral_win[0], numeral_win[1], numeral_win[2], 1, 0); }
  arrow_window();
}
module rings_2d() for (r = ring_r) difference() { difference() { circle(r = r + groove_w/2, $fn = 240); circle(r = r - groove_w/2, $fn = 240); } arrow_keepout(); }
module text_rules_2d() { for (r = rule_r) { arc2d(r - groove_w/2, r + groove_w/2, 90 - 33, 90 + 33, 120); arc2d(r - groove_w/2, r + groove_w/2, 270 - 44, 270 + 44, 120); } arc_text("WREN & CO.", true); arc_text("SURVEYOR'S PLATE", false); }
module clear_of_windows() difference() { children(); offset(delta = keep_off) window_tops_2d(); }
module raised_3d() translate([0, 0, topz()]) {
  clear_of_windows() linear_extrude(h_ring) rings_2d();
  clear_of_windows() linear_extrude(h_text) text_rules_2d();
}
module flat_plate() difference() { sight_plate(); notches_3d(); }       // brass body: V2b's body with NO engraving
// print orientation as modelled = FACE UP (bosses/cups hang below, facing the bed)
if (part == "m72v2r_brass_up") translate([0, 0, -(plate_z0 - 1.3)]) flat_plate();   // lowest boss face at z=0 (bosses hang 1.3 mm below the body)
if (part == "m72v2r_black_up") translate([0, 0, -(plate_z0 - 1.3)]) raised_3d();
if (part == "m72v2r_view") translate([0, 0, -plate_z0]) { color("#c9a24a") flat_plate(); color("#101014") raised_3d(); }
// ---- checks (EMPTY = pass) ----
if (part == "chk_v2r_windows") intersection() { raised_3d(); translate([0, 0, topz() - 1]) linear_extrude(3) window_tops_2d(); }        // raised features never over a window/chamfer
if (part == "chk_v2r_parts") union() { intersection() { raised_3d(); translate([0, 0, z_cap + 1.2]) cover(); } intersection() { raised_3d(); translate([0, 0, z_floor]) { outer_ring(); inner_ring(); } } intersection() { raised_3d(); translate([0, 0, z_cap]) index_cap(); } }
if (part == "chk_v2r_overhang") difference() { linear_extrude(topz() + 2) union() { rings_2d(); text_rules_2d(); }  translate([0, 0, -1]) linear_extrude(topz() + 3) offset(delta = 0.0) difference() { circle(r = plate_ro, $fn = 160); circle(r = plate_ri, $fn = 160); } }  // raised footprint must lie on the plate top: EMPTY
echo(raised_top_z = topz() + max(h_text, h_ring), body_top_z = topz());
