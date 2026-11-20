// M-72 SURVEYOR'S OBSERVATION PLATE V2 (Keeper handoff 20 Nov): cosmetic and usability refinement of the V1 test plate.
// V1 (m72_sight_plate_concept.scad) is kept untouched as the rollback. V2 ONLY REMOVES material from V1's top face and rim: the windows, cups,
// bosses, body, outline and everything the physical test validated are unchanged. NON-PRODUCTION until Keeper/owner approve.
include <m72_sight_plate_concept.scad>

dec_depth = 0.4;      // engraving depth (two 0.2 mm layers) in the 2.0 mm plate body
groove_w  = 0.5;      // concentric groove width
txt_size  = 4.6;      // OpenSCAD text size: capital height is 0.91 x size = about 4.2 mm
txt_track = 0.5;      // extra letter spacing, mm
txt_font  = "Liberation Serif:style=Bold";   // serif-inspired, period-appropriate
em = 1.374*txt_size;  // measured: OpenSCAD's em for this font is 1.374 x size
cap_h = 0.909*txt_size;
r_base_up = 53.0;     // upper title: baseline radius (letters stand outward, caps end at about r 57.2)
r_base_lo = 57.2;     // lower title: baseline radius (letters read left to right with their tops toward the centre, caps end at about r 53.0)
ring_r = [40.6, 41.4, 47.6, 48.4];   // concentric grooves in the web between the symbol and numeral windows
rule_r = [51.8, 58.4];               // thin arc rules framing each title

cw = [["W",1.0],["R",0.722],["E",0.667],["N",0.722],["&",0.833],["C",0.722],["O",0.778],[".",0.25],["S",0.556],["U",0.722],["V",0.722],["Y",0.722],["P",0.611],["L",0.667],["A",0.722],["T",0.667],["'",0.278],[" ",0.25]];
function wi(c) = [for (e = cw) if (e[0] == c) e[1]][0]*em;
function lens(s) = [for (k = [0:len(s) - 1]) wi(s[k]) + (k < len(s) - 1 ? txt_track : 0)];
function cum(l, k) = k == 0 ? 0 : cum(l, k - 1) + l[k - 1];
module arc_text(s, upper) {
  l = lens(s); tot = cum(l, len(s) - 1) + wi(s[len(s) - 1]);
  rb = upper ? r_base_up : r_base_lo;
  rm = rb + (upper ? cap_h/2 : -cap_h/2);
  for (k = [0:len(s) - 1]) if (s[k] != " ") {
    sc = cum(l, k) + wi(s[k])/2;
    ph = upper ? 90 + (tot/2 - sc)/rm*180/PI : 270 + (sc - tot/2)/rm*180/PI;
    translate([rb*cos(ph), rb*sin(ph)]) rotate(upper ? ph - 90 : ph - 270) text(s[k], size = txt_size, font = txt_font, halign = "center", valign = "baseline");
  }
}
module decor_2d() {
  for (r = ring_r) difference() { circle(r = r + groove_w/2, $fn = 240); circle(r = r - groove_w/2, $fn = 240); }
  for (r = rule_r) { arc2d(r - groove_w/2, r + groove_w/2, 90 - 33, 90 + 33, 120); arc2d(r - groove_w/2, r + groove_w/2, 270 - 44, 270 + 44, 120); }
  arc_text("WREN & CO.", true);
  arc_text("SURVEYOR'S PLATE", false);
}
module notches_3d() for (a = [0, 180, 270, 87, 93]) rotate([0, 0, a]) translate([plate_ro, 0, plate_z0 - 1]) rotate([0, 0, 45]) cube([1.8, 1.8, plate_t + 2]);   // the Chronometer's own rim-notch shape and positions
module sight_plate_v2(dz = 0) translate([0, 0, dz]) difference() {
  sight_plate();
  translate([0, 0, plate_z0 + plate_t - dec_depth]) linear_extrude(dec_depth + 0.1) decor_2d();
  notches_3d();
}
if (part == "m72v2_plate") sight_plate_v2();
if (part == "m72v2_plate_print") rotate([180, 0, 0]) translate([0, 0, -(plate_z0 + plate_t)]) sight_plate_v2();   // TOP FACE DOWN, as V1
if (part == "m72v2_top") rotate([0, 0, 0]) translate([0, 0, -plate_z0]) color("#c9a24a") sight_plate_v2();      // viewing orientation: top face up
// ---- V2 checks ----
if (part == "chk_v2_adds_nothing") difference() { sight_plate_v2(); sight_plate(); }       // EMPTY: V2 only removes material from V1
if (part == "chk_v2_rings") intersection() { sight_plate_v2(); translate([0, 0, z_floor]) { outer_ring(); inner_ring(); } }
if (part == "chk_v2_cap") intersection() { sight_plate_v2(); translate([0, 0, z_cap]) index_cap(); }
if (part == "chk_v2_cover") intersection() { sight_plate_v2(); translate([0, 0, z_cap + 1.2]) cover(); }
if (part == "chk_v2_heads") intersection() { sight_plate_v2(); heads_at_assembly(); }
if (part == "chk_v2_stops") intersection() { sight_plate_v2(-0.1); heads_at_assembly(); }                 // SOLID: the heads still hold the plate up
// notch vs window walls: the smallest wall left between any rim notch and a window (printed as a number)
echo(notch_to_window_min_deg = min([for (n = [0, 180, 270, 87, 93], w = [330, 210, 150]) abs(((n - w + 180) % 360) - 180)]));
// ---- V2b: the same engraving, FILLED with a second colour (black), printed as two bodies like the back plate and the tile digits ----
// The inlay is exactly the engraved volume (0.4 mm = two layers at the bed), so the colour change is at layer 3. Import 'brass part' and 'black part' together as ONE object.
module inlay_3d() intersection() { sight_plate(); translate([0, 0, plate_z0 + plate_t - dec_depth]) linear_extrude(dec_depth) decor_2d(); }
if (part == "m72v2b_black_print") rotate([180, 0, 0]) translate([0, 0, -(plate_z0 + plate_t)]) inlay_3d();
if (part == "m72v2b_brass_print") rotate([180, 0, 0]) translate([0, 0, -(plate_z0 + plate_t)]) sight_plate_v2();
if (part == "chk_v2b_overfill") difference() { union() { sight_plate_v2(); inlay_3d(); } sight_plate(); }                       // EMPTY: nothing added outside the original plate
if (part == "chk_v2b_gap") difference() { difference() { sight_plate(); notches_3d(); } union() { sight_plate_v2(); inlay_3d(); } }   // EMPTY: the two bodies fill the plate completely
if (part == "m72v2b_view") translate([0, 0, -plate_z0]) { color("#c9a24a") sight_plate_v2(); color("#1b1b1f") inlay_3d(); }
if (part == "m72v2b_view2") translate([0, 0, -plate_z0]) { color("#c9a24a") difference() { sight_plate(); notches_3d(); } color("#101014") translate([0, 0, 0.05]) inlay_3d(); }
