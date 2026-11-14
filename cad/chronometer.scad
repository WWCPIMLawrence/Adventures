// ============================================================================
//  THE CHRONOMETER  -  parametric puzzle instrument            (OpenSCAD 2021+)
//  Units: mm.  Angles: degrees, CCW from +X.  12 o'clock = +Y (90 deg).
//  Clock position k (0 = XII, 1 = I ...) sits at angle 90 - 30*k.
//  Z = 0 is the back face (the face that lies on the clue sheet).
//
//  Pick a part with `part`, or run ./build.sh to export everything.
// ============================================================================

/* [View / export] */
part = "assembly"; // [assembly, exploded, section, base, test_base, test_seat, test_screw_ring, test_uv_bay, deck, outer_ring, inner_ring, index_cap, pawl_outer, pawl_inner, cover, keystone, mask, uv_ring, door, fragment_1, fragment_2, fragment_3, fragment_4, plate_small_parts, plate_springs, plate_fragments]

/* [Envelope] */
body_r   = 62.5;   // outer radius of the instrument
well_r   = 25.0;   // radius of the central well / aperture
edge_ch  = 0.8;    // comfort chamfer on outer edges

/* [Fits - tune these after the test print] */
ring_clear    = 0.30;  // radial clearance, ring journal to hub / rib
ring_axial    = 0.35;  // axial play of ring flange under the index cap (0.35-0.40 for the first prototype)
cover_clear   = 0.20;  // radial clearance, cover skirt in well
mask_clear    = 0.30;  // radial clearance, mask disc in well
door_clear    = 0.20;  // per-side clearance, UV door in its dovetail
frag_clear    = 0.20;  // radial clearance, fragment pegs in cover holes

/* [Ring deck] */
deck_t     = 2.0;    // deck floor thickness
rib_h      = 3.0;    // height of hub and of the fixed rib between rings
hub_r      = 28.0;   // hub outer radius (inner-ring journal)
rib_ri     = 42.0;   // fixed rib inner radius
rib_ro     = 48.0;   // fixed rib outer radius (outer-ring journal)
cap_ri     = 40.0;   // index cap inner radius
cap_ro     = 50.0;   // index cap outer radius
cap_t      = 2.4;    // index cap thickness
ring_h     = 5.6;    // total ring height
flange_h   = rib_h - ring_axial; // ring flange height (part trapped under cap)

/* [Detents] */
positions     = 12;
pawl_span     = 36;    // angular length of a pawl spring, deg
pawl_t        = 1.2;   // spring beam thickness: 1.0 soft, 1.2 medium, 1.4 firm
pawl_h        = 2.7;   // pawl height
pawl_wall     = 1.2;   // rib wall left between pawl pocket and ring
pawl_foot     = 1.0;   // spring travel available behind the beam (at pawl_t = 1.2)
notch_depth   = 0.6;   // depth of detent scallops in the rings
notch_r       = 2.0;   // scallop radius
nose_r        = 1.5;   // pawl nose tip radius
nose_w        = 4.4;   // pawl nose base width
pawl_preload  = 0.15;  // nose interference when seated in a notch
outer_pawl_angles = [60, 240];
inner_pawl_angles = [120, 300];

/* [Hardware] */
screw_angles  = [30, 150, 270];  // index-cap screws
screw_r       = 45.0;            // radius of the screw circle
screw_clear_d = 3.4;             // M3 clearance hole
screw_pilot_d = 2.8;             // M3 self-tapping pilot in PLA (4.0-4.2 for heat-set inserts)
screw_pilot_depth = 14;          // maximum; the pilot is capped at base height - 1.5 mm
cap_screw_len = 16;              // M3x16 socket-head cap screws (checked below)
knob_screw_len = 8;              // M3x8 socket-head cap screw in the keystone (checked below)
cap_screw_style = "cap";         // [cap: socket-head sits proud, csk: countersunk flush]
nut_af        = 5.7;             // M3 nut across flats + fit
nut_t         = 2.4;

/* [Centre cover] */
cover_r       = 27.8;   // flange radius
cover_proud   = 3.0;    // how far the cover stands above the ring faces (finger grip)
skirt_wall    = 1.6;
bay_lug_w     = 10;     // bayonet lug angular width, deg
bay_travel    = 28;     // bayonet twist, deg (clockwise from above to lock)
bay_lug_r     = 1.4;    // lug radial projection
bay_entry_angles = [270, 35, 150];  // unequal spacing = one orientation only
bay_play_free = 0.75;   // axial play at start of twist
bay_play_end  = 0.50;   // axial play at the locked position - a running fit, NOT a friction lock.
                        // Test history (PLA, outer wall first): 0.45/0.30 bound; 0.90/0.70 free with a
                        // visible lift; 0.70/0.40 bound again. The 45 deg ceiling droops roughly 0.4 mm
                        // when its overhanging wall is printed first. With walls printed inner-first,
                        // 0.75/0.50 (seat A) turns easily, clicks at both ends and has no wiggle;
                        // 0.95/0.70 (seat B) is free but wiggles about 1 mm. A is the setting.
bay_floor_relief = 0.3; // relief cut in the base top under the lugs' path (adds to the 0.25 mm gap)
// Transport retention is a sprung latch: the free end of the UV retaining ring carries a nub
// that passes through a slot in the cover skirt and clicks into a groove in the well wall.
latch_angle   = 60;     // where the latch sits when the cover is locked
latch_depth   = 1.1;    // groove depth in the well wall = spring travel (0.7: no click; 0.9: very faint)
latch_groove_r = 1.6;   // groove radius: smaller = steeper flanks = sharper click (nub tip is r 1.2)
uv_ring_h     = 2.4;    // height of the retaining ring / latch spring
uv_ring_w     = 2.1;    // radial thickness of the ring (latch stiffness); PETG only

/* [Keystone knob] */
knob_r        = 10.0;
knob_h        = 7.0;
knob_head_d   = 5.4;    // press-fit bore for the M3 socket head
knob_head_h   = 3.2;
knob_clamp_gap = 0.3;   // knob underside stays this far off the cover when its cone is seated on
                        // the fragment bevels, so the screw load goes into the tiles
nut_retain    = 0.35;   // the mouth of the nut pocket is this much under size: the nut is drawn
                        // in with a screw once and cannot drop out afterwards

/* [Fragments] */
frag_t        = 2.4;
frag_ro       = 25.8;
frag_ri       = 6.6;    // inner radius at the bottom face (45 deg bevel above it)
frag_gap      = 1.0;    // gap between neighbouring fragments
peg_d         = 3.6;
peg_h         = 2.3;
peg_angle     = 24;     // pegs sit at +/- this angle from the fragment centre line
peg_radii_a   = [13.0, 15.5, 18.0, 20.5];   // unique per fragment = keying
peg_radii_b   = [20.5, 18.0, 15.5, 13.0];
// 12 characters, clockwise from the XII position. Fragment n carries three of them.
// Approved game configuration: SUN at the arrow; MOON, STAR, HOURGLASS, DIAMOND (positions
// I, IV, VII, X) read 1-1-4-7. Tiles carry 281 / 361 / 924 / 507.
code_ring     = ["8","1","3","6","1","9","2","4","5","0","7","2"];
frag_text_r   = 19.5;
frag_text_h   = 6.5;
frag_font     = "Liberation Sans:style=Bold";

/* [Aperture mask] */
mask_t        = 1.2;
ledge_t       = 0.8;    // floor ledge the mask sits on (sets mask height above the paper)
ledge_r       = 22.0;   // clear opening under the mask
aperture_d    = 10.5;
// aperture centres [x, y]; demo = T-I-M-E clockwise from the top
apertures     = [[0, 15], [15, 0], [0, -15], [-15, 0]];
sight_d       = 2.5;    // centre sighting hole (0 = none)
mask_style    = "spring"; // [spring: three spring arms grip the well, dropin: loose keyed disc with a finger notch]
mask_key_angle = 270;   // must equal one of bay_entry_angles
mask_key_w    = 3.0;
mask_key_r    = 26.2;

/* [UV flashlight compartment] */
// Flat squeeze-type coin-cell key-fob light, lying on its face. Caliper-measured with the
// key ring removed: 1.5855 in long (LED included), 0.8900 in wide, 0.3410 in thick.
// For a round light set uv_w = uv_t = its diameter.
uv_w        = 22.6;   // widest point across the body
uv_t        = 8.7;    // thickness, face to face (the squeeze switch is on a face)
uv_len      = 40.3;   // overall length including the LED
uv_clear    = 1.5;    // total side-to-side clearance (felt on the side walls stops rattle)
uv_z_clear  = 1.5;    // total face clearance - keeps door and roof OFF the squeeze switch
uv_end_gap  = 1.0;    // free space at each end
bay_y       = 41.5;   // distance of bay centre line from instrument centre
bay_x       = 3.5;    // shift of bay along its own length (toward the door exit)
door_t      = 2.0;    // door thickness
uv_enabled  = true;   // false = no bay and no door (issue the light as a separate prop)
base_plain_h = 11;    // base height when uv_enabled is false

/* [Decoration] */
show_numerals = true;
numeral_h     = 6.0;
knurl_n       = 60;

/* [Hidden] */
$fn = 48;
fn_big = 144;
eps = 0.01;

// ---------------------------------------------------------------- derived ---
bay_w     = uv_w + uv_clear;
bay_len   = uv_len + 2*uv_end_gap;
door_wb   = bay_w;                 // door width at the back face
door_wt   = door_wb + 2*door_t;    // door width at its inner face (45 deg dovetail)
door_ceil = 0.5;                   // clearance above the door (bridged ceiling)
door_x0   = bay_x - bay_len/2 - 2.5;
base_h    = uv_enabled ? door_t + uv_t + uv_z_clear : base_plain_h;
test_base_h = 11;

cover_seat_z = deck_t + rib_h;                    // in deck coordinates
cover_t   = (ring_h - rib_h) + cover_proud;
skirt_ro  = well_r - cover_clear;
skirt_ri  = skirt_ro - skirt_wall;
skirt_len = cover_seat_z - 0.25;
bay_groove_r = well_r + bay_lug_r + 0.2;

outer_ring_ri_low = rib_ro + ring_clear;          // journal surface
outer_ring_ri_top = cap_ro + 0.3;
inner_ring_ri     = hub_r + ring_clear;           // journal surface
inner_ring_ro_low = rib_ri - 0.35;
inner_ring_ro_top = cap_ri - 0.3;

// pawl geometry (see pawl())
po_wall_face = rib_ro - pawl_wall;                         // outer pawls
po_back      = po_wall_face - 0.25 - 1.2 - pawl_foot;
po_tip       = outer_ring_ri_low + notch_depth + pawl_preload;
pi_wall_face = rib_ri + pawl_wall;                         // inner pawls
pi_back      = pi_wall_face + 0.25 + 1.2 + pawl_foot;
pi_tip       = inner_ring_ro_low - notch_depth - pawl_preload;

z_deck  = base_h;
z_floor = z_deck + deck_t;
z_cap   = z_floor + rib_h;
z_cover_top = z_cap + cover_t;

// ------------------------------------------------------------ sanity echo ---
echo(str("Base height ", base_h, " mm; rim height ", z_floor + ring_h,
         " mm; height over keystone ", z_cover_top + knob_h, " mm"));
_corner_r = norm([abs(door_x0) + door_clear, bay_y + door_wt/2 + door_clear]);
if (_corner_r > body_r - 2.0)
  echo(str("WARNING: UV door slot is within ", body_r - _corner_r,
           " mm of the rim - shorten uv_len, shift bay_x, or enlarge body_r"));
if (bay_y - door_wt/2 - door_clear < well_r + 2.0)
  echo("WARNING: UV door slot is too close to the central well - increase bay_y");
// hardware self-check: cap screws must reach >= 6 mm of thread without bottoming out; the
// keystone screw must pass fully through the nut with the fragments fitted
_cap_stack = cap_t + rib_h + deck_t;
_cap_pilot = min(screw_pilot_depth, base_h - 1.5);
_cap_thread = cap_screw_len - _cap_stack;
echo(str("Cap screws: M3x", cap_screw_len, " - ", _cap_stack, " mm clearance stack, ", _cap_thread,
         " mm of thread in a ", _cap_pilot, " mm pilot"));
if (_cap_thread > _cap_pilot - 0.5) echo("WARNING: cap screws bottom out in the base - use a shorter screw");
if (_cap_thread < 6) echo("WARNING: cap screws have under 6 mm of thread - use a longer screw");
_knob_reach = knob_screw_len - (knob_h - knob_head_h) - knob_clamp_gap;   // below the cover face, fragments fitted
_nut_bottom = 1.4 + nut_t;                                                 // below the cover face
echo(str("Keystone screw: M3x", knob_screw_len, " reaches ", _knob_reach, " mm below the cover face; nut spans 1.4 to ",
         _nut_bottom, " mm"));
if (_knob_reach < _nut_bottom - 0.3) echo("WARNING: keystone screw does not pass fully through the nut");
if (_knob_reach + knob_clamp_gap > cover_t + skirt_len - 0.5) echo("WARNING: keystone screw is too long");
for (a = screw_angles)
  if (abs(screw_r*sin(a) - bay_y) < door_wt/2 + 3 && abs(screw_r*cos(a) - bay_x) < bay_len/2 + 6)
    echo(str("WARNING: screw at ", a, " deg collides with the UV bay"));

// ---------------------------------------------------------------- helpers ---
function arc_pts(r, a0, a1, n = 32) =
  [for (i = [0:n]) let (a = a0 + (a1 - a0)*i/n) [r*cos(a), r*sin(a)]];
module arc2d(ri, ro, a0, a1, n = 32)
  polygon(concat(arc_pts(ro, a0, a1, n), arc_pts(ri, a1, a0, n)));
module wedge2d(r, a0, a1) polygon(concat([[0, 0]], arc_pts(r, a0, a1, 32)));
module ring2d(ro, ri) difference() { circle(r = ro, $fn = fn_big); circle(r = ri, $fn = fn_big); }
module rev(pts) rotate_extrude($fn = fn_big) polygon(pts);
module rev_sector(a0, da, pts) rotate([0, 0, a0]) rotate_extrude(angle = da, $fn = fn_big) polygon(pts);
function clock_angle(k) = 90 - 30*k;
module seg(p, q, w) hull() { translate(p) circle(d = w, $fn = 8); translate(q) circle(d = w, $fn = 8); }

// --------------------------------------------------------- Roman numerals ---
ROMAN = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"];
function _gw(c, H, sw) = c == "I" ? sw : 0.5*H;
function _gx(s, i, H, sw) = i <= 0 ? 0 : _gx(s, i - 1, H, sw) + _gw(s[i - 1], H, sw) + 0.16*H;
module roman2d(s, H = 6, sw = 0.9) {
  n = len(s);
  W = _gx(s, n - 1, H, sw) + _gw(s[n - 1], H, sw);
  translate([-W/2, -H/2]) {
    for (i = [0:n - 1]) translate([_gx(s, i, H, sw), 0]) {
      w = _gw(s[i], H, sw);
      if (s[i] == "I") seg([w/2, 0], [w/2, H], sw);
      if (s[i] == "V") { seg([0, H], [w/2, 0], sw); seg([w, H], [w/2, 0], sw); }
      if (s[i] == "X") { seg([0, H], [w, 0], sw); seg([0, 0], [w, H], sw); }
    }
    seg([-0.6, 0], [W + 0.6, 0], 0.7);   // foot rail
    seg([-0.6, H], [W + 0.6, H], 0.7);   // head rail
  }
}

// =================================================================== BASE ===
// Rear module: mask seat, sheet-registration notches, UV bay + door slot.
module base(h = base_h, with_uv = uv_enabled) {
  zc = ledge_t + mask_t/2;
  pilot = min(screw_pilot_depth, h - 1.5);
  difference() {
    rev([[ledge_r, 0], [body_r - edge_ch, 0], [body_r, edge_ch], [body_r, h - 0.4], [body_r - 0.4, h],
         [well_r + 0.6, h], [well_r, h - 0.6],
         [well_r, zc + 0.5], [well_r + 0.25, zc], [well_r, zc - 0.5],   // click groove for mask springs
         [well_r, ledge_t], [ledge_r, ledge_t]]);
    // floor relief under the cover lugs, only where the deck's recess is open above it (a relief
    // under solid deck would be an unsupported ceiling in the one-piece seat test print)
    for (a = bay_entry_angles)
      rev_sector(a - bay_travel - bay_lug_w/2 - 0.3, bay_travel + bay_lug_w + 1.8,
                 [[well_r - 1, h - bay_floor_relief], [bay_groove_r, h - bay_floor_relief], [bay_groove_r, h + 1], [well_r - 1, h + 1]]);
    // mask keyway
    rotate([0, 0, mask_key_angle]) translate([well_r - 1, -(mask_key_w + 0.6)/2, ledge_t])
      cube([mask_key_r + 0.3 - well_r + 1, mask_key_w + 0.6, h]);
    // self-tapping pilots for the cap screws
    for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, h - pilot])
      cylinder(d = screw_pilot_d, h = pilot + 1, $fn = 24);
    // sheet registration notches: 12 o'clock is a double notch
    for (a = [0, 180, 270, 87, 93]) rotate([0, 0, a]) translate([body_r, 0, -1])
      rotate([0, 0, 45]) cube([1.8, 1.8, h + 2], center = false);
    if (with_uv) translate([bay_x, bay_y, 0]) {
      c = door_clear;
      // flashlight bay (open to the deck above; 45 deg lead-out above the door)
      rotate([90, 0, 90]) linear_extrude(bay_len, center = true)
        polygon([[-door_wt/2 - c, door_t], [door_wt/2 + c, door_t],
                 [bay_w/2, door_t + door_wt/2 + c - bay_w/2], [bay_w/2, h + 1],
                 [-bay_w/2, h + 1], [-bay_w/2, door_t + door_wt/2 + c - bay_w/2]]);
      // dovetail slot for the door, exits through the rim on +X
      translate([door_x0 - bay_x, 0, 0]) rotate([90, 0, 90]) linear_extrude(2*body_r)
        polygon([[-door_wb/2 - c, -eps], [door_wb/2 + c, -eps], [door_wt/2 + c, door_t],
                 [door_wt/2 + c, door_t + door_ceil], [-door_wt/2 - c, door_t + door_ceil],
                 [-door_wt/2 - c, door_t]]);
      // detent notch for the door's side spring
      translate([-bay_x, -c, 0]) flank_bump(door_nub_x, 4.0, door_nub_h + 0.05);
    }
  }
}

// bump / notch that follows the 45 deg dovetail flank on the -Y side of the door
door_nub_x = 45.5;
door_nub_h = 1.1;   // latch nub height on the door's side spring (0.7 barely caught: the door's
                    // 0.4 mm of side play ate most of it)
module flank_bump(xc, len, d)
  multmatrix([[1, 0, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    translate([xc, -door_wb/2, 0]) linear_extrude(door_t)
      polygon([[-len/2 - d, eps], [-len/2, -d], [len/2, -d], [len/2 + d, eps]]);

// ================================================================== DOOR ====
module door() {
  beam_w = 2.4; xa = 27; xb = 48;      // longer, wider spring: more travel at lower strain
  translate([bay_x, bay_y, 0]) difference() {
    union() {
      intersection() {
        translate([door_x0 - bay_x + door_clear, 0, 0]) rotate([90, 0, 90]) linear_extrude(2*body_r)
          polygon([[-door_wb/2, 0], [door_wb/2, 0], [door_wt/2, door_t], [-door_wt/2, door_t]]);
        translate([-bay_x, -bay_y, 0])
          rev([[0, -1], [body_r - edge_ch - 1, -1], [body_r, edge_ch], [body_r, door_t + 1], [0, door_t + 1]]);
      }
      translate([-bay_x, 0, 0]) flank_bump(door_nub_x, 3.0, door_nub_h);
    }
    // side spring: slot + end cut
    translate([xa - bay_x, -door_wb/2 + beam_w, -1]) cube([xb - xa + 0.8, 0.8, door_t + 2]);
    translate([xb - bay_x, -door_wt/2 - 2, -1]) cube([0.8, door_wt/2 + 2 - door_wb/2 + beam_w + 0.8, door_t + 2]);
    // thumb grooves on the back face
    for (i = [0:3]) translate([22 + 3*i - bay_x, -3, -eps]) cube([1.0, 9, 0.4]);
  }
}

// ================================================================== DECK ====
// Ring deck: hub + fixed rib (journals), pawl pockets, bayonet seat for the cover.
module deck() {
  top = deck_t + rib_h;
  difference() {
    union() {
      rev([[well_r, 0], [body_r - 0.4, 0], [body_r, 0.4], [body_r, deck_t], [well_r, deck_t]]);
      translate([0, 0, deck_t - eps]) linear_extrude(rib_h + eps) {
        ring2d(hub_r, well_r);
        ring2d(rib_ro, rib_ri);
      }
    }
    // cap screws
    for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, -1])
      cylinder(d = screw_clear_d, h = top + 2, $fn = 24);
    // pawl pockets + nose windows
    translate([0, 0, deck_t]) linear_extrude(rib_h + 1) {
      for (a = outer_pawl_angles) rotate([0, 0, a]) {
        arc2d(po_back, po_wall_face, -pawl_span/2 - 0.5, pawl_span/2 + 0.5);
        arc2d(po_wall_face - 0.1, rib_ro + 0.1, -4, 4);
      }
      for (a = inner_pawl_angles) rotate([0, 0, a]) {
        arc2d(pi_wall_face, pi_back, -pawl_span/2 - 0.5, pawl_span/2 + 0.5);
        arc2d(rib_ri - 0.1, pi_wall_face + 0.1, -4.6, 4.6);
      }
    }
    // bayonet: entry grooves (also the passage for the mask key tab)
    for (a = bay_entry_angles) rotate([0, 0, a]) translate([0, 0, -1]) linear_extrude(top + 2)
      arc2d(well_r - 0.5, bay_groove_r, -bay_lug_w/2 - 1.5, bay_lug_w/2 + 1.5);
    // latch grooves in the well wall: one at the locked position, one at the insert position
    for (a = [latch_angle, latch_angle + bay_travel]) rotate([0, 0, a])
      translate([well_r + latch_depth - latch_groove_r, 0, deck_t]) cylinder(r = latch_groove_r, h = rib_h + 1, $fn = 32);
    // bayonet: locking recess with 45 deg ceiling, ramping down to bay_play_end
    for (a = bay_entry_angles) {
      a_stop = a - bay_travel - bay_lug_w/2 - 0.3;      // hard stop
      a_dwell = a - bay_travel + bay_lug_w/2;           // tight zone for the seated lug
      a_open = a - bay_lug_w/2;
      n = 6;
      bay_recess(a_stop, a_dwell - a_stop, bay_play_end);
      for (i = [0:n - 1])
        bay_recess(a_dwell + (a_open - a_dwell)*i/n - 0.01, (a_open - a_dwell)/n + 0.02,
                   bay_play_end + (bay_play_free - bay_play_end)*(i + 1)/n);
    }
  }
}
// lug chamfer line is r + z = well_r - cover_clear + bay_lug_r + 1.5 (deck coords)
bay_line = well_r - cover_clear + bay_lug_r + 1.5;
module bay_recess(a0, da, play)
  rev_sector(a0, da, [[well_r - 0.5, -1], [bay_groove_r, -1],
                      [bay_groove_r, bay_line + play - bay_groove_r],
                      [well_r - 0.5, bay_line + play - well_r + 0.5]]);

// ================================================================= RINGS ====
module outer_ring() {
  difference() {
    rev([[outer_ring_ri_low + 0.4, 0], [body_r - 0.4, 0], [body_r, 0.4], [body_r, ring_h - 1.0],
         [body_r - 1.0, ring_h], [outer_ring_ri_top, ring_h], [outer_ring_ri_top, flange_h],
         [outer_ring_ri_low, flange_h], [outer_ring_ri_low, 0.4]]);
    // detent scallops on the journal surface
    for (k = [0:positions - 1]) rotate([0, 0, k*360/positions])
      translate([outer_ring_ri_low + notch_depth - notch_r, 0, -1]) cylinder(r = notch_r, h = flange_h + 1);
    // rim knurl
    for (k = [0:knurl_n - 1]) rotate([0, 0, (k + 0.5)*360/knurl_n])
      translate([body_r + 0.9, 0, -1]) cylinder(r = 1.5, h = ring_h + 2, $fn = 16);
    // hour numerals
    if (show_numerals) for (k = [0:11]) rotate([0, 0, clock_angle(k)])
      translate([(outer_ring_ri_top + body_r - 1.6)/2, 0, ring_h - 0.5]) rotate([0, 0, -90])
        linear_extrude(1) roman2d(ROMAN[k], numeral_h);
  }
}

module inner_ring() {
  lab_ri = inner_ring_ri + 1.2; lab_ro = inner_ring_ro_top - 1.2;
  difference() {
    rev([[inner_ring_ri, 0], [inner_ring_ro_low - 0.4, 0], [inner_ring_ro_low, 0.4],
         [inner_ring_ro_low, flange_h], [inner_ring_ro_top, flange_h], [inner_ring_ro_top, ring_h - 0.4],
         [inner_ring_ro_top - 0.4, ring_h], [inner_ring_ri + 0.4, ring_h], [inner_ring_ri, ring_h - 0.4]]);
    for (k = [0:positions - 1]) rotate([0, 0, k*360/positions])
      translate([inner_ring_ro_low - notch_depth + notch_r, 0, -1]) cylinder(r = notch_r, h = flange_h + 1);
    // 0.4 mm label pockets for replaceable symbol stickers
    for (k = [0:11]) rotate([0, 0, clock_angle(k)]) translate([0, 0, ring_h - 0.4])
      linear_extrude(1) arc2d(lab_ri, lab_ro, -12.5, 12.5, 12);
  }
  // raised finger ribs between positions
  for (k = [0:11]) rotate([0, 0, clock_angle(k) + 15]) translate([lab_ri, -0.8, ring_h - 0.2])
    cube([lab_ro - lab_ri, 1.6, 1.0]);
}

// ============================================================= INDEX CAP ====
// Fixed ring between the two dials: traps both ring flanges and the pawls,
// carries the reference index at 12 o'clock.
module index_cap() {
  difference() {
    rev([[cap_ri, 0], [cap_ro, 0], [cap_ro, cap_t - 0.4], [cap_ro - 0.4, cap_t],
         [cap_ri + 0.4, cap_t], [cap_ri, cap_t - 0.4]]);
    for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, -1]) {
      cylinder(d = screw_clear_d, h = cap_t + 2, $fn = 24);
      if (cap_screw_style == "csk") translate([0, 0, cap_t + 1 - 1.7]) cylinder(d1 = 3.0, d2 = 6.4, h = 1.7 + eps, $fn = 32);
    }
    // index: double arrow pointing at both rings
    translate([0, 0, cap_t - 0.6]) linear_extrude(1) rotate([0, 0, 90]) {
      polygon([[cap_ro - 0.8, 0], [screw_r + 0.6, 2.2], [screw_r + 0.6, -2.2]]);
      polygon([[cap_ri + 0.8, 0], [screw_r - 0.6, 2.2], [screw_r - 0.6, -2.2]]);
    }
  }
}

// ================================================================= PAWLS ====
// Arc-shaped leaf spring, supported on two feet, nose in the middle.
// Drawn centred on +X; lives in a pocket of the fixed rib.
module pawl(outward = true, t = pawl_t) {
  half = pawl_span/2 - 0.3; fd = 3.5;
  linear_extrude(pawl_h) if (outward) {
    r2 = po_wall_face - 0.25; r1 = r2 - t;
    arc2d(r1, r2, -half, half);
    for (s = [-1, 1]) rotate([0, 0, s*(half - fd/2)]) arc2d(po_back + 0.05, r1 + eps, -fd/2, fd/2, 6);
    hull() {
      translate([r2 - 0.3, -nose_w/2]) square([0.3, nose_w]);
      translate([po_tip - nose_r, 0]) circle(r = nose_r, $fn = 32);
    }
  } else {
    r1 = pi_wall_face + 0.25; r2 = r1 + t;
    arc2d(r1, r2, -half, half);
    for (s = [-1, 1]) rotate([0, 0, s*(half - fd/2)]) arc2d(r2 - eps, pi_back - 0.05, -fd/2, fd/2, 6);
    hull() {
      translate([r1, -nose_w/2]) square([0.3, nose_w]);
      translate([pi_tip + nose_r, 0]) circle(r = nose_r, $fn = 32);
    }
  }
}

// ================================================================= COVER ====
// Local z = 0 is the underside of the flange (sits on the hub top).
// Drawn in its LOCKED orientation. Print upside-down (face on the plate).
module cover() {
  lug_z0 = -skirt_len;
  difference() {
    union() {
      rev([[0, 0], [cover_r, 0], [cover_r, cover_t - 0.8], [cover_r - 0.8, cover_t], [0, cover_t]]);
      rev([[skirt_ri, -skirt_len], [skirt_ro, -skirt_len], [skirt_ro, eps], [skirt_ri, eps]]);
      for (a = bay_entry_angles)
        rev_sector(a - bay_travel - bay_lug_w/2, bay_lug_w,
                   [[skirt_ro - 0.2, lug_z0], [skirt_ro + bay_lug_r, lug_z0],
                    [skirt_ro + bay_lug_r, lug_z0 + 1.25], [skirt_ro - 0.2, lug_z0 + 1.25 + bay_lug_r + 0.2]]);
    }
    // grip scallops
    for (k = [0:35]) rotate([0, 0, k*10 + 5]) translate([cover_r + 0.8, 0, -1])
      cylinder(r = 1.4, h = cover_t + 2, $fn = 16);
    // M3 nut trap (from below) and screw hole for the keystone
    translate([0, 0, cover_t - 1.4 - nut_t - 0.2]) cylinder(d = nut_af/cos(30), h = nut_t + 0.2, $fn = 6);
    translate([0, 0, -eps]) cylinder(d = (nut_af - nut_retain)/cos(30), h = cover_t - 1.4 - nut_t, $fn = 6);
    // slot in the skirt for the latch nub
    rotate([0, 0, latch_angle]) translate([skirt_ri - 1, -2.3, -skirt_len - 1]) cube([skirt_wall + 2, 4.6, skirt_len + 1]);
    cylinder(d = 3.4, h = cover_t + 1, $fn = 24);
    // keyed sockets for the four fragments
    for (i = [0:3]) for (p = frag_peg_pos(i)) translate([p[0], p[1], cover_t - peg_h - 0.3])
      cylinder(d = peg_d + 2*frag_clear, h = peg_h + 1, $fn = 24);
    // 12 o'clock mark
    translate([0, cover_r - 3.2, cover_t - 0.5]) linear_extrude(1) polygon([[-1.3, 0], [1.3, 0], [0, 2.0]]);
  }
}

// split ring that holds the UV-reactive paper disc inside the cover skirt
module uv_ring() {
  ro = skirt_ri + 0.1; tip = well_r + latch_depth - 0.05;
  linear_extrude(uv_ring_h) {
    arc2d(ro - uv_ring_w, ro, latch_angle - 5, latch_angle + 325, 96);
    // latch nub on the free end: the last ~13 mm of the ring is the spring
    rotate([0, 0, latch_angle]) hull() {
      translate([ro - 0.4, -1.6]) square([0.4, 3.2]);
      translate([tip - 1.2, 0]) circle(r = 1.2, $fn = 24);
    }
  }
}

// knob that screws into the cover and clamps the fragments by their bevels. Its cone matches
// the fragment bevel exactly and meets it while the flat underside is still knob_clamp_gap
// above the cover; with no fragments fitted it simply screws down onto the cover.
module keystone() {
  difference() {
    rev([[0, 0], [frag_ri + knob_clamp_gap, 0], [knob_r, knob_r - frag_ri - knob_clamp_gap], [knob_r, knob_h - 0.6],
         [knob_r - 0.6, knob_h], [0, knob_h]]);
    translate([0, 0, -1]) cylinder(d = 3.4, h = knob_h + 2, $fn = 24);
    translate([0, 0, knob_h - knob_head_h]) cylinder(d = knob_head_d, h = knob_head_h + 1, $fn = 32);
    for (k = [0:15]) rotate([0, 0, k*22.5]) translate([knob_r + 0.7, 0, 2])
      cylinder(r = 1.3, h = knob_h, $fn = 16);
  }
}

// ============================================================= FRAGMENTS ====
function frag_centre(i) = 90 - 90*i;        // fragment 0 at XII, 1 at III, 2 at VI, 3 at IX
function frag_peg_pos(i) = let (c = frag_centre(i))
  [[peg_radii_a[i]*cos(c + peg_angle), peg_radii_a[i]*sin(c + peg_angle)],
   [peg_radii_b[i]*cos(c - peg_angle), peg_radii_b[i]*sin(c - peg_angle)]];

// Drawn in place on the cover face (local z = 0). Print upside-down (text on the plate).
module fragment(i) {
  c = frag_centre(i);
  difference() {
    intersection() {
      rev([[frag_ri, 0], [frag_ro, 0], [frag_ro, frag_t - 0.4], [frag_ro - 0.4, frag_t],
           [frag_ri + frag_t, frag_t]]);
      linear_extrude(frag_t) offset(delta = -frag_gap/2) wedge2d(40, c - 45, c + 45);
    }
    // three code characters, tops outward
    for (j = [-1, 0, 1]) rotate([0, 0, clock_angle(3*i + j)]) translate([frag_text_r, 0, frag_t - 0.5])
      rotate([0, 0, -90]) linear_extrude(1)
        text(code_ring[(3*i + j + 12) % 12], size = frag_text_h, font = frag_font, halign = "center", valign = "center");
    // order pips (1-4)
    for (n = [0:i]) rotate([0, 0, c]) translate([12.0, (n - i/2)*2.4, frag_t - 0.4]) cylinder(d = 1.3, h = 1, $fn = 12);
  }
  for (p = frag_peg_pos(i)) translate([p[0], p[1], -peg_h])
    cylinder(d1 = peg_d - 0.8, d2 = peg_d, h = 0.4 + eps, $fn = 24);
  for (p = frag_peg_pos(i)) translate([p[0], p[1], -peg_h + 0.4]) cylinder(d = peg_d, h = peg_h - 0.4 + eps, $fn = 24);
}

// ================================================================== MASK ====
// Opaque stencil. Three in-plane spring arms grip the well wall; one key tab
// fixes rotation. Push it out from the back with a finger to swap it.
module mask() {
  r = well_r - mask_clear; arm_w = 1.6; slot = 0.8; arm_deg = 30;
  spring = mask_style == "spring";
  spring_angles = [mask_key_angle + 60, mask_key_angle + 180, mask_key_angle + 300];
  difference() {
    linear_extrude(mask_t) difference() {
      union() {
        circle(r = r, $fn = fn_big);
        rotate([0, 0, mask_key_angle]) translate([r - 2, -mask_key_w/2]) square([mask_key_r - r + 2, mask_key_w]);
        if (spring) for (a = spring_angles) rotate([0, 0, a + arm_deg/2 - 3]) translate([r - 0.75, 0]) circle(r = 1.4, $fn = 24);
      }
      if (spring) for (a = spring_angles) rotate([0, 0, a]) {
        arc2d(r - arm_w - slot, r - arm_w, -arm_deg/2, arm_deg/2 + 2);
        rotate([0, 0, arm_deg/2]) arc2d(r - arm_w - slot, r + 2, 0, 2.2, 4);
      }
      // drop-in version: finger notch opposite the key (stays over the ledge, so nothing shows)
      if (!spring) rotate([0, 0, mask_key_angle + 180]) translate([r + 3.2, 0]) circle(r = 5.6, $fn = 48);
      for (p = apertures) translate(p) circle(d = aperture_d, $fn = 64);
      if (sight_d > 0) circle(d = sight_d, $fn = 24);
    }
    // "top" marker above the first aperture
    translate([0, 0, mask_t - 0.4]) linear_extrude(1)
      translate([0, apertures[0][1] + aperture_d/2 + 0.8]) polygon([[-1.2, 0], [1.2, 0], [0, 1.8]]);
  }
}

// ============================================================== ASSEMBLY ====
C_BRASS = [0.72, 0.58, 0.30]; C_DARK = [0.16, 0.17, 0.20]; C_IVORY = [0.90, 0.87, 0.78];
C_STEEL = [0.55, 0.57, 0.60]; C_RED = [0.55, 0.12, 0.10];

module screw(len, head = true) color(C_STEEL) {
  translate([0, 0, -len]) cylinder(d = 2.9, h = len, $fn = 16);
  if (head) cylinder(d = 5.5, h = 3, $fn = 24);
}

module assembly(e = 0, fragments = true, cover_on = true, door_out = 0, light = false) {
  color(C_BRASS) base();
  if (uv_enabled) translate([door_out, 0, -1.2*e]) color(C_DARK) door();
  if (light) translate([bay_x + (door_out > 0 ? 6 : 0), bay_y, door_t + 0.3 - (door_out > 0 ? 16 : 0)]) uv_light();
  translate([0, 0, ledge_t + 0.35*e]) color(C_DARK) mask();
  translate([0, 0, z_deck + e]) color(C_BRASS) deck();
  translate([0, 0, z_floor + 1.5*e]) {
    color(C_RED) for (a = outer_pawl_angles) rotate([0, 0, a]) pawl(true);
    color(C_RED) for (a = inner_pawl_angles) rotate([0, 0, a]) pawl(false);
  }
  translate([0, 0, z_floor + 2*e]) color(C_DARK) outer_ring();
  translate([0, 0, z_floor + 2*e]) color(C_IVORY) inner_ring();
  translate([0, 0, z_cap + 2.6*e]) {
    color(C_BRASS) index_cap();
    for (a = screw_angles) rotate([0, 0, a]) translate([screw_r, 0, cap_t + 0.6*e]) screw(cap_screw_len);
  }
  if (cover_on) translate([0, 0, z_cap + 3.6*e]) {
    color(C_BRASS) cover();
    translate([0, 0, -uv_ring_h - 0.3 - 0.3*e]) color(C_DARK) uv_ring();
    if (fragments) translate([0, 0, cover_t + 0.5*e]) color(C_IVORY) for (i = [0:3]) fragment(i);
    translate([0, 0, cover_t + (fragments ? knob_clamp_gap : 0) + 1.2*e]) {
      color(C_DARK) keystone();
      translate([0, 0, knob_h - knob_head_h + 0.6*e]) screw(knob_screw_len);
    }
  }
}

// visual stand-in for the squeeze light (not a printed part)
module uv_light() {
  color([0.45, 0.2, 0.7]) hull() {
    translate([-uv_len/2 + 5, 0, 0]) cylinder(d = 10, h = uv_t - 1);
    translate([-4, 0, 0]) scale([1.3, 1, 1]) cylinder(d = uv_w, h = uv_t);
    translate([uv_len/2 - 9, 0, 0]) cylinder(d = 10, h = uv_t - 1);
  }
  color([0.9, 0.9, 1]) translate([uv_len/2 - 6, 0, uv_t/2]) rotate([0, 90, 0]) cylinder(d = 5, h = 6);
}

// ================================================================ OUTPUT ====
if (part == "assembly") assembly();
if (part == "exploded") assembly(e = 14);
if (part == "view_start") assembly(fragments = false);                    // as handed to players
if (part == "view_aperture") assembly(cover_on = false);                  // cover removed
if (part == "view_uv") assembly(fragments = false, door_out = 58, light = true);
if (part == "section") difference() { assembly(); translate([0, -200, -50]) cube([200, 400, 200]); }
if (part == "base") base();
if (part == "test_base") base(h = test_base_h, with_uv = false);
// short fit test for the cover bayonet, the latch and the mask: centre of deck + base in one piece
test_mark = 0;   // number of notches cut in the rim of the seat test piece, to tell variants apart
if (part == "test_seat") difference() { intersection() {
  cylinder(r = 33, h = 40, $fn = fn_big);
  union() { base(h = 4, with_uv = false); translate([0, 0, 4 - eps]) deck(); }
}
  for (k = [0:1:test_mark - 1]) rotate([0, 0, 180 + k*12]) translate([33, 0, -1]) cylinder(r = 2, h = 40, $fn = 24); }
// light backing ring for the ring/detent test: gives the three cap screws something to tap
// into without printing a whole base
if (part == "test_screw_ring") intersection() {
  base(h = test_base_h, with_uv = false);
  linear_extrude(test_base_h + 1) ring2d(screw_r + 6.5, screw_r - 6.5);
}
// fit test for the flashlight bay and door: just that corner of the base
if (part == "test_uv_bay") intersection() {
  base(with_uv = true);
  translate([door_x0 - 5, bay_y - door_wt/2 - 4, -1]) cube([200, 200, 100]);
}
// close-up check of the fragment clamp: a thin slice through the centre, one colour per part
// (exported as 2D cuts, one per part, and drawn by scripts/clamp_section.py)
clamp_item = 0;
if (part == "clamp_section") projection(cut = true) rotate([-90, 0, 0]) {
  if (clamp_item == 0) cover();
  if (clamp_item == 1) translate([0, 0, cover_t]) for (i = [0:3]) fragment(i);
  if (clamp_item == 2) translate([0, 0, cover_t + knob_clamp_gap]) keystone();
  if (clamp_item == 3) translate([0, 0, cover_t + knob_clamp_gap + knob_h - knob_head_h]) { translate([0, 0, -8]) cylinder(d = 2.9, h = 8, $fn = 16); cylinder(d = 5.5, h = 3, $fn = 24); }
  if (clamp_item == 4) translate([0, 0, cover_t - 1.4 - nut_t])
    difference() { cylinder(d = 5.5/cos(30), h = nut_t, $fn = 6); translate([0, 0, -1]) cylinder(d = 2.9, h = 5); }
}

if (part == "deck") deck();
if (part == "outer_ring") outer_ring();
if (part == "inner_ring") inner_ring();
if (part == "index_cap") index_cap();
if (part == "pawl_outer") pawl(true);
if (part == "pawl_inner") pawl(false);
if (part == "cover") rotate([180, 0, 0]) translate([0, 0, -cover_t]) cover();          // print orientation
if (part == "keystone") rotate([180, 0, 0]) translate([0, 0, -knob_h]) keystone();     // print orientation
if (part == "mask") mask();
if (part == "uv_ring") uv_ring();
if (part == "door") translate([-bay_x, -bay_y, 0]) door();
for (i = [0:3]) if (part == str("fragment_", i + 1))
  rotate([180, 0, 0]) translate([0, 0, -frag_t]) fragment(i);                           // print orientation
if (part == "plate_fragments")
  for (i = [0:3]) translate([(i % 2)*42, floor(i/2)*26, 0]) rotate([180, 0, 0]) translate([0, -16, -frag_t])
    rotate([0, 0, 90 - frag_centre(i)]) fragment(i);
// spring plates: two of each pawl in three stiffnesses (1.0 / 1.2 / 1.4 mm, left to right,
// marked with 1 / 2 / 3 bars beside them). plate_small_parts adds the keystone and is meant
// for PLA; plate_springs has two latch rings and no keystone and is meant for PETG.
module spring_set() for (n = [0:2]) {
  for (m = [0:1]) {
    translate([-po_back + n*7, m*32 - 16, 0]) pawl(true, 1.0 + 0.2*n);
    translate([-pi_back + 30 + n*7, m*32 - 16, 0]) rotate([0, 0, 180]) mirror([1, 0, 0]) pawl(false, 1.0 + 0.2*n);
  }
  for (k = [0:n]) translate([n*7 - 1 + k*1.6, -38, 0]) cube([0.9, 5, 0.6]);        // stiffness marks
  for (k = [0:n]) translate([30 + n*7 - 1 + k*1.6, -38, 0]) cube([0.9, 5, 0.6]);
}
if (part == "plate_small_parts") {
  spring_set();
  translate([-45, 0, 0]) uv_ring();
  translate([-45, 0, 0]) rotate([180, 0, 0]) translate([0, 0, -knob_h]) keystone();
}
if (part == "plate_springs") {
  spring_set();
  translate([-45, 0, 0]) uv_ring();
  translate([-45, 52, 0]) uv_ring();
}

// ---- interference checks (see build.sh): each of these must render EMPTY ----
module at_floor() translate([0, 0, z_floor]) children();
if (part == "chk_rings_deck") intersection() { translate([0, 0, z_deck]) deck(); at_floor() { outer_ring(); inner_ring(); } }
if (part == "chk_rings_cap") intersection() { translate([0, 0, z_cap]) index_cap(); at_floor() { outer_ring(); inner_ring(); } }
if (part == "chk_rings_cover") intersection() { translate([0, 0, z_cap]) cover(); at_floor() inner_ring(); }
if (part == "chk_cover_deck") intersection() { translate([0, 0, z_cap]) cover(); translate([0, 0, z_deck]) deck(); }
if (part == "chk_cover_base") intersection() { translate([0, 0, z_cap]) cover(); base(); }
if (part == "chk_cover_insert") intersection() {   // cover in the lift-out position must also be free
  translate([0, 0, z_cap + 2]) rotate([0, 0, bay_travel]) cover(); translate([0, 0, z_deck]) deck(); }
if (part == "chk_pawls_deck") intersection() { translate([0, 0, z_deck]) deck();
  at_floor() { for (a = outer_pawl_angles) rotate([0, 0, a]) pawl(true); for (a = inner_pawl_angles) rotate([0, 0, a]) pawl(false); } }
if (part == "chk_pawls_cap") intersection() { translate([0, 0, z_cap]) index_cap();
  at_floor() { for (a = outer_pawl_angles) rotate([0, 0, a]) pawl(true); for (a = inner_pawl_angles) rotate([0, 0, a]) pawl(false); } }
if (part == "chk_door_base") intersection() { base(); door(); }
if (part == "chk_mask_base") intersection() { base(); translate([0, 0, ledge_t]) linear_extrude(mask_t) circle(r = well_r - mask_clear); }
if (part == "chk_frag_cover") intersection() { cover(); translate([0, 0, cover_t]) for (i = [0:3]) fragment(i); }
if (part == "chk_frag_knob") intersection() { translate([0, 0, knob_clamp_gap]) keystone(); for (i = [0:3]) fragment(i); }
// knob underside must still be clear of the cover when the cone is seated on the tiles
if (part == "chk_knob_cover") intersection() { translate([0, 0, cover_t + knob_clamp_gap]) keystone(); cover(); }
// clamp proof: 0.1 mm further down the cone must bite into the tiles (non-empty)
if (part == "chk_clamp") intersection() { translate([0, 0, knob_clamp_gap - 0.1]) keystone(); for (i = [0:3]) fragment(i); }
// the whole 28 deg turning path of the cover, not just its end positions: the flange and
// skirt are bodies of revolution, so the swept volume is those plus each lug smeared over the turn
module cover_swept() {
  rev([[0, 0], [cover_r, 0], [cover_r, cover_t], [0, cover_t]]);
  rev([[skirt_ri, -skirt_len], [skirt_ro, -skirt_len], [skirt_ro, eps], [skirt_ri, eps]]);
  for (a = bay_entry_angles)
    rev_sector(a - bay_travel - bay_lug_w/2, bay_lug_w + bay_travel,
               [[skirt_ro - 0.2, -skirt_len], [skirt_ro + bay_lug_r, -skirt_len],
                [skirt_ro + bay_lug_r, -skirt_len + 1.25], [skirt_ro - 0.2, -skirt_len + 1.25 + bay_lug_r + 0.2]]);
}
if (part == "chk_cover_path") intersection() { translate([0, 0, z_deck]) deck(); translate([0, 0, z_cap]) cover_swept(); }
if (part == "chk_cover_path_base") intersection() { base(); translate([0, 0, z_cap]) cover_swept(); }
// latch: free in its groove when locked and at the insert position, compressed in between (non-empty)
module latch_at(a) translate([0, 0, z_cap - uv_ring_h - 0.3]) rotate([0, 0, a]) uv_ring();
if (part == "chk_latch_locked") intersection() { translate([0, 0, z_deck]) deck(); union() { latch_at(0); latch_at(bay_travel); } }
if (part == "chk_latch_mid") intersection() { translate([0, 0, z_deck]) deck(); latch_at(bay_travel/2); }
if (part == "chk_latch_cover") intersection() { cover(); translate([0, 0, -uv_ring_h - 0.3]) uv_ring(); }
// the real mask: its spring nubs must press on the well wall (non-empty), nothing else may touch
if (part == "chk_mask_springs") intersection() { base(); translate([0, 0, ledge_t]) mask(); }
if (part == "chk_frag_frag") intersection() { union() { fragment(0); fragment(2); } union() { fragment(1); fragment(3); } }
// wrong-socket test: fragment 1 rotated into socket 2 must COLLIDE (non-empty)
if (part == "chk_keying") intersection() { cover(); translate([0, 0, cover_t]) rotate([0, 0, -90]) fragment(0); }
// detent engagement: pawl noses must OVERLAP the ring notches by the preload (non-empty)
if (part == "chk_detent") intersection() { outer_ring(); for (a = outer_pawl_angles) rotate([0, 0, a]) pawl(true); }
