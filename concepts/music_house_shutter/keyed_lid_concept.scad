// NON-PRODUCTION CONCEPT: captive keyed lid for the integrated back plate (Music House KEY).
// Includes the real Chronometer CAD only to test fit. Nothing here changes, replaces or is read by the approved design.
include <../../cad/chronometer.scad>

// ---- the lid: a solid disc that sits on the floor over all four holes, three bayonet lugs, a square clock arbor ----
lid_r = 22.4;            // covers every hole (the furthest hole edge is 20.25 from the centre)
lid_z0 = plate_floor_t + 0.2; lid_t = 1.0;        // rests 0.2 above the floor top (1.2), 1.0 thick
lug_r = 23.9; lug_w = 26; lug_t = 0.6;            // three bayonet lugs, 26 deg wide
hub_d = 10; hub_h = 3.2; sock = 4.2; sock_d = 2.6;  // centre hub with a RECESSED square socket: nothing to grip with a fingernail
// ---- the receiver: three hooks standing inside the plate's well (the well is r 25; nothing of the base is inside it) ----
hook_r0 = 24.2; hook_r1 = 24.75;                  // post: 0.55 mm thick, 0.25 mm clear of the well wall
hook_z1 = 3.1; over_r0 = 22.8; over_z0 = 2.5;     // overhang arm: 0.6 thick, reaches in to r 22.8
hook_w = 44; hook_a0 = 30;                        // 44 deg arcs starting at 30, 150, 270 deg (CAD angles)
lock_c = 30;                                      // lug centre inside the hook when locked (deg after the hook start)
// ---- the key: a clock-winding key with a square tongue and a T handle ----
key_tongue = 4.0; key_tongue_len = 5.0; key_od = 12;

module arc3(r0, r1, a0, w, h) rotate([0, 0, a0]) rotate_extrude(angle = w, $fn = 120) translate([r0, 0]) square([r1 - r0, h]);
module hooks() for (k = [0:2]) rotate([0, 0, 120*k]) {
  translate([0, 0, plate_floor_t - 0.01]) arc3(hook_r0, hook_r1, hook_a0, hook_w, hook_z1 - plate_floor_t + 0.01);   // post
  translate([0, 0, over_z0]) arc3(over_r0, hook_r1, hook_a0, hook_w, hook_z1 - over_z0);                            // overhang arm
}
module lid(a = 0) rotate([0, 0, a]) {   // disc + lugs (the hub and socket are added in lid_full)
  translate([0, 0, lid_z0]) cylinder(r = lid_r, h = lid_t, $fn = 120);
  for (k = [0:2]) rotate([0, 0, 120*k + hook_a0 + lock_c - lug_w/2]) translate([0, 0, lid_z0]) arc3(lid_r - 0.1, lug_r, 0, lug_w, lug_t);
}
module lid_full(a = 0) rotate([0, 0, a]) difference() {
  union() { lid(0); translate([0, 0, lid_z0]) cylinder(d = hub_d, h = hub_h, $fn = 48); }
  translate([-sock/2, -sock/2, lid_z0 + hub_h - sock_d]) cube([sock, sock, sock_d + 0.01]);
}
module key() union() {
  translate([0, 0, key_tongue_len]) { cylinder(d = key_od, h = 6, $fn = 48); translate([-18, -2.5, 0]) cube([36, 5, 6]); }   // T handle above the tongue
  translate([-key_tongue/2, -key_tongue/2, 0]) cube([key_tongue, key_tongue, key_tongue_len + 0.01]);
}
// the replacement plate = the approved plate plus the three hooks (floor, holes and everything else unchanged)
module plate_with_hooks() { back_plate(); hooks(); }
unlock_a = 30 + 32 + 4;      // turn needed to bring each lug into the gap between hooks (about 32 deg beyond the hook end), plus margin
if (part == "kl_plate") plate_with_hooks();
if (part == "kl_lid") lid_full();
if (part == "kl_key") key();
// ---- fit and function checks ----
if (part == "chk_kl_added_in_holes") intersection() { hooks(); translate([0, 0, -1]) linear_extrude(plate_floor_t + 5) { for (p = ap_pts) translate(p) circle(d = aperture_d, $fn = 64); circle(d = sight_d, $fn = 24); } }   // EMPTY: the apertures are untouched
if (part == "chk_kl_hooks_base") intersection() { translate([0, 0, 0]) hooks(); union() { translate([0, 0, z_deck]) deck(); base(); } }               // EMPTY: the hooks stay inside the well
if (part == "chk_kl_hooks_cover") intersection() { hooks(); translate([0, 0, z_cap]) cover(); }                                                             // EMPTY
if (part == "chk_kl_free_turn") union() for (a = [0:5:359]) intersection() { lid_full(a); plate_with_hooks(); }                                                  // locked-height lid must turn freely about the plate: lugs only touch hooks by being under them; at rest height EMPTY
if (part == "chk_kl_locked_lift") intersection() { translate([0, 0, 1.0]) lid_full(0); hooks(); }                                                                  // SOLID: lifted 1.0 mm while locked, the hooks stop the lid
if (part == "chk_kl_unlocked_lift") intersection() { translate([0, 0, 8]) lid_full(unlock_a); hooks(); }                                                           // EMPTY: turned to the gap, it lifts straight out
if (part == "chk_kl_key_arbor") intersection() { translate([0, 0, lid_z0 + hub_h - sock_d]) key(); lid_full(); }                                                       // the key's tongue dropped into the socket must NOT overlap the lid (EMPTY: the socket is bigger than the tongue)
if (part == "chk_kl_arbor_under_cover") intersection() { lid_full(); translate([0, 0, z_cap]) cover(); }                                                          // EMPTY: the arbor stays clear of the cover
if (part == "kl_view") { color("#c9a24a") plate_with_hooks(); color("#2b2d33") lid_full(0); }
if (part == "kl_view_open") { color("#c9a24a") plate_with_hooks(); color("#2b2d33") translate([0, 0, 14]) lid_full(unlock_a); color("#b03a2e") translate([0, 0, 22]) key(); }
