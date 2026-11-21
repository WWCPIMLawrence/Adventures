// M-72 SURVEYOR'S OBSERVATION PLATE V2c (Keeper handoff 21 Nov): PRINT-QUALITY refinement of V2b. NON-PRODUCTION until the owner's test print is judged.
// V2b (m72_sight_plate_V2.scad + files 14c/14d) is untouched and stays the fallback. V2c changes ONLY the decoration (what is engraved/inlaid in the top 0.4 mm):
//   * rings: the two PAIRS of 0.5 mm lines (0.3 mm brass gap between them, narrower than the nozzle) become two single 0.8 mm lines;
//   * rule arcs 0.5 -> 0.8 mm;
//   * lettering: same font, wording, positions; glyphs grown by 0.12 mm all round (hairlines/serifs thicker, corners rounded) and drawn at size 4.35 so the
//     overall letter height stays about the same; letter spacing +0.2 mm.
// Plate body, windows, chamfers, cups, bosses, notches, outline: IDENTICAL to V1/V2/V2b (this file only redefines the decoration).
include <m72_sight_plate_V2.scad>

groove_w  = 0.8;                 // decorative line width (V2b: 0.5)
ring_r    = [41.0, 48.0];        // two continuous rings (V2b: 40.6, 41.4, 47.6, 48.4); each exactly covers the old pair's outer span 40.6-41.4 / 47.6-48.4
rule_r    = [51.8, 58.4];        // arc rules unchanged in position, now 0.8 wide
txt_size  = 4.35;                // V2b 4.6; with the 0.12 growth the cap height is 0.909*4.35 + 0.24 = 4.19 mm (V2b 4.18)
txt_track = 0.7;                 // V2b 0.5
glyph_grow = 0.12;               // per-side growth of every glyph

module glyph(c) offset(r = glyph_grow) text(c, size = txt_size, font = txt_font, halign = "center", valign = "baseline");
module arc_text(s, upper, only = -1) {
  l = lens(s); tot = cum(l, len(s) - 1) + wi(s[len(s) - 1]);
  rb = upper ? r_base_up : r_base_lo;
  rm = rb + (upper ? cap_h/2 : -cap_h/2);
  for (k = [0:len(s) - 1]) if (s[k] != " " && (only < 0 || only == k)) {
    sc = cum(l, k) + wi(s[k])/2;
    ph = upper ? 90 + (tot/2 - sc)/rm*180/PI : 270 + (sc - tot/2)/rm*180/PI;
    translate([rb*cos(ph), rb*sin(ph)]) rotate(upper ? ph - 90 : ph - 270) glyph(s[k]);
  }
}
// the rings stop 0.5 mm short of the fixed-arrow window's sides (V2b: the ring grazed the window edge and left thin black slivers)
module arrow_keepout() rotate([0, 0, 90]) translate([40.0, -5.0]) square([10.6, 10.0]);
module decor_2d() {
  for (r = ring_r) difference() { difference() { circle(r = r + groove_w/2, $fn = 240); circle(r = r - groove_w/2, $fn = 240); } arrow_keepout(); }
  for (r = rule_r) { arc2d(r - groove_w/2, r + groove_w/2, 90 - 33, 90 + 33, 120); arc2d(r - groove_w/2, r + groove_w/2, 270 - 44, 270 + 44, 120); }
  arc_text("WREN & CO.", true);
  arc_text("SURVEYOR'S PLATE", false);
}
// ---- V2c parts (same orientation as V2b: TOP FACE DOWN) ----
if (part == "m72v2c_black_print") rotate([180, 0, 0]) translate([0, 0, -(plate_z0 + plate_t)]) inlay_3d();
if (part == "m72v2c_brass_print") rotate([180, 0, 0]) translate([0, 0, -(plate_z0 + plate_t)]) sight_plate_v2();
if (part == "m72v2c_view") translate([0, 0, -plate_z0]) { color("#c9a24a") sight_plate_v2(); color("#1b1b1f") inlay_3d(); }
if (part == "m72v2c_view2") translate([0, 0, -plate_z0]) { color("#c9a24a") difference() { sight_plate(); notches_3d(); } color("#101014") translate([0, 0, 0.05]) inlay_3d(); }
// ---- V2c checks (all must be EMPTY) ----
if (part == "chk_v2c_adds_nothing") difference() { union() { sight_plate_v2(); inlay_3d(); } sight_plate(); }     // nothing outside the original body
if (part == "chk_v2c_gap") difference() { difference() { sight_plate(); notches_3d(); } union() { sight_plate_v2(); inlay_3d(); } }
if (part == "chk_v2c_vs_V2b_body") difference() { sight_plate_v2(); difference() { sight_plate(); notches_3d(); } }   // brass body never gains material
// glyph gap check: adjacent letters closer than gap_min (default 0.30 mm) show as non-empty
gap_min = 0.30;
module pair_gap(s, upper) for (k = [0:len(s) - 2]) if (s[k] != " " && s[k+1] != " ")
  intersection() { offset(delta = gap_min/2) arc_text(s, upper, k); offset(delta = gap_min/2) arc_text(s, upper, k + 1); }
if (part == "chk_v2c_letter_gaps") linear_extrude(0.4) { pair_gap("WREN & CO.", true); pair_gap("SURVEYOR'S PLATE", false); }
// thin black slivers where the decoration meets window chamfers/outline (2-D cut at mid-depth of the inlay); opening radius 0.2 = nothing thinner than 0.4 mm
module inlay_slice() projection(cut = true) translate([0, 0, -(plate_z0 + plate_t - dec_depth/2)]) inlay_3d();
if (part == "chk_v2c_slivers") linear_extrude(0.4) difference() { inlay_slice(); offset(r = 0.2) offset(delta = -0.2) inlay_slice(); }
