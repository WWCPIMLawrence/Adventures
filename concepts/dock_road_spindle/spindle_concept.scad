// NON-PRODUCTION CONCEPT (Keeper feasibility request, 19 Nov): hexagonal winding spindle for the Dock Road recording strip.
// Includes the real Chronometer CAD only to test fit. Nothing here changes, replaces or is read by the approved design.
include <../../cad/chronometer.scad>
sp_af   = 11.0;    // across flats of the winding faces
sp_len  = 40.0;    // overall length including the end lips
sp_lip  = 0.8;     // end lips stand this far proud of the faces on every side (strip end retention)
sp_lip_t = 1.6;    // lip thickness along the axis
sp_edge = 0.7;     // rounding radius on the hex corners
sp_slit_w = 0.7;   // strip anchor: a slit cut radially into face 1 (paper or film tail tucks in)
sp_slit_d = 3.0;
sp_x = 0; sp_y = 0; sp_rot = 0;   // placement for the fit checks: lying on its face on the plate floor
module hex2d(af) rotate(30) offset(r = sp_edge) offset(delta = -sp_edge) circle(d = af/cos(30), $fn = 6);   // rotated so a flat faces +X
module spindle() {   // axis along +Z, faces start at angle 0 (face 1 is the +X flat); print it standing up
  difference() {
    union() {
      linear_extrude(sp_len) hex2d(sp_af);                                    // winding faces
      for (z = [0, sp_len - sp_lip_t]) translate([0, 0, z]) linear_extrude(sp_lip_t) hex2d(sp_af + 2*sp_lip);   // end lips
    }
    // end chamfers so no corner is sharp
    for (e = [0, 1]) translate([0, 0, e ? sp_len : 0]) rotate([e ? 180 : 0, 0, 0]) difference() {
      translate([0, 0, -1]) cylinder(r = 50, h = 1.6, $fn = 8);
      translate([0, 0, 0]) rotate(30) cylinder(r1 = (sp_af + 2*sp_lip)/2/cos(30) - 0.6, r2 = (sp_af + 2*sp_lip)/2/cos(30) + 1.2, h = 0.6, $fn = 6);
    }
    // strip anchor: radial slit into face 1 (the +X flat), clear of the lips
    translate([sp_af/2 - sp_slit_d, -sp_slit_w/2, sp_lip_t + 1]) cube([sp_slit_d + 1, sp_slit_w, sp_len - 2*sp_lip_t - 2]);
    // starting orientation: a V notch in the lip at face 1 (both ends) so face 1 is found by touch and sight
    for (z = [-0.01, sp_len - sp_lip_t - 0.01]) translate([sp_af/2 + sp_lip, 0, z]) rotate([0, 0, 0]) linear_extrude(sp_lip_t + 0.02) polygon([[0.01, -1.1], [-1.4, 0], [0.01, 1.1]]);
  }
}
// lying on its face on the plate floor (floor top 1.2), axis along X
module spindle_lying() translate([sp_x, sp_y, plate_floor_t + 0.02]) rotate([0, 0, sp_rot]) translate([0, 0, (sp_af + 2*sp_lip)/2]) rotate([0, 90, 0]) rotate([0, 0, 0]) translate([0, 0, -sp_len/2]) spindle();
// the things it must clear (assembly positions): base, deck, back plate, cover with ring and the knob screw tip
module fixed_parts() { back_plate(); base(); translate([0, 0, z_deck]) deck(); }
module cover_parts() { translate([0, 0, z_cap]) cover(); translate([0, 0, z_cap - uv_ring_h - 0.3]) uv_ring(); translate([0, 0, z_cap - 1.1]) cylinder(d = 2.9, h = 10, $fn = 16); }
if (part == "spindle") spindle();
if (part == "chk_sp_open") intersection() { spindle_lying(); fixed_parts(); }                 // EMPTY: fits in the open well (cover off)
if (part == "chk_sp_covered") intersection() { spindle_lying(); union() { fixed_parts(); cover_parts(); } }     // EMPTY: fits under the seated cover
if (part == "sp_view") { color("#c9a24a") fixed_parts(); color("#2b2d33") cover_parts(); color("#b03a2e") spindle_lying(); }
if (part == "sp_lying") spindle_lying();
