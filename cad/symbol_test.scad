// ============================================================================
//  CHRONOMETER - printed dial-symbol test plate            (OpenSCAD 2021+)
//  Stand-alone experiment. It does not include or modify chronometer.scad.
//
//  Four rows of the twelve dial symbols, printed face UP like the inner ring:
//    row 1 (one dot)    flush two-colour inlay, 6 mm symbols
//    row 2 (two dots)   flush two-colour inlay, 7 mm symbols
//    row 3 (three dots) recessed 0.4 mm for paint-fill, 6 mm symbols
//    row 4 (four dots)  recessed 0.6 mm for paint-fill, 6 mm symbols
//    row 5 (five dots)  RAISED 0.4 mm in black, 7 mm symbols (or print in one colour and
//                       colour the tops with an acrylic marker)
//  Symbol order, left to right = clockwise on the dial:
//    sun moon key flame star wave mountain hourglass tree compass diamond eye
//
//  part = "body"  -> the bone-white plate (cavities for the inlays, open recesses)
//  part = "inlay" -> the black inlays for rows 1 and 2 only
//  Import both STLs into Bambu Studio together as ONE object with two parts.
// ============================================================================

part = "preview"; // [preview, body, inlay]

/* [Plate] */
plate_t     = 2.0;    // plate thickness
pitch       = 10.0;   // spacing between symbols
row_pitch   = 11.0;
margin      = 6.0;

/* [Symbols] */
inlay_depth = 0.4;    // two 0.2 mm layers of black: opaque, and only 4 filament changes
rows = [              // [kind, symbol size, depth]
  ["inlay", 6.0, inlay_depth],
  ["inlay", 7.0, inlay_depth],
  ["recess", 6.0, 0.4],
  ["recess", 6.0, 0.6],
  ["raised", 7.0, 0.4]];

/* [Hidden] */
$fn = 40;
eps = 0.01;
NAMES = ["sun", "moon", "key", "flame", "star", "wave", "mountain", "hourglass", "tree", "compass", "diamond", "eye"];

// ---------------------------------------------------------------- symbols ---
// Each symbol is drawn in a box of +/-1 unit, upright, and scaled to size/2.
// Rule for a 0.4 mm nozzle at 6 mm: no solid feature thinner than 0.2 units (0.6 mm)
// and no gap narrower than 0.17 units (0.5 mm).
module seg(p, q, w) hull() { translate(p) circle(d = w); translate(q) circle(d = w); }

module sym_sun() {
  circle(r = 0.44);
  for (k = [0:7]) rotate(45*k) translate([0.66, -0.11]) square([0.34, 0.22]);
}
module sym_moon() difference() { circle(r = 0.92); translate([0.46, 0.14]) circle(r = 0.78); }
module sym_key() {
  difference() { translate([0, 0.55]) circle(r = 0.45); translate([0, 0.55]) circle(r = 0.2); }
  translate([-0.13, -1]) square([0.26, 1.15]);
  translate([0, -1]) square([0.5, 0.24]);
  translate([0, -0.56]) square([0.38, 0.22]);
}
module sym_flame() difference() {
  union() {
    hull() { translate([0.05, -0.38]) circle(r = 0.62); translate([0.22, 0.95]) circle(r = 0.05); }
    hull() { translate([-0.3, -0.3]) circle(r = 0.42); translate([-0.62, 0.5]) circle(r = 0.05); }
  }
  hull() { translate([0.05, -0.5]) circle(r = 0.25); translate([0.1, 0.1]) circle(r = 0.04); }
}
module sym_star()
  polygon([for (k = [0:9]) let (r = k % 2 == 0 ? 1 : 0.42, a = 90 + 36*k) [r*cos(a), r*sin(a)]]);
module sym_wave() for (y0 = [-0.4, 0.4])
  for (i = [0:15]) seg([-0.88 + i*0.11, y0 + 0.22*sin(360*(i*0.11)/0.88)],
                       [-0.88 + (i + 1)*0.11, y0 + 0.22*sin(360*((i + 1)*0.11)/0.88)], 0.26);
module sym_mountain()
  polygon([[-1, -0.75], [-0.32, 0.85], [0.14, -0.02], [0.46, 0.38], [1, -0.75]]);
module sym_hourglass() {
  polygon([[-0.6, 0.8], [0.6, 0.8], [0.1, 0], [0.6, -0.8], [-0.6, -0.8], [-0.1, 0]]);
  for (y = [-1, 0.78]) translate([-0.8, y]) square([1.6, 0.22]);
}
module sym_tree() {
  for (c = [[-0.4, 0.18, 0.42], [0.4, 0.18, 0.42], [0, 0.55, 0.45], [0, 0.15, 0.4]]) translate([c[0], c[1]]) circle(r = c[2]);
  translate([-0.14, -0.8]) square([0.28, 0.8]);
  translate([-0.6, -1]) square([1.2, 0.22]);
}
module sym_compass() {
  difference() { circle(r = 0.95); circle(r = 0.72); }
  polygon([[0, 0.52], [0.24, 0], [0, -0.52], [-0.24, 0]]);   // 0.2 units clear of the ring
}
module sym_diamond() polygon([[0, 1], [0.66, 0], [0, -1], [-0.66, 0]]);
module sym_eye() {
  module lens(r) intersection() { translate([0, -r + 0.62]) circle(r = r, $fn = 80); translate([0, r - 0.62]) circle(r = r, $fn = 80); }
  difference() { lens(1.1); offset(delta = -0.2) lens(1.1); }
  circle(r = 0.26);                                  // 0.16 units clear of the outline
}
module symbol(i, size) scale(size/2) {
  if (i == 0) sym_sun();       if (i == 1) sym_moon();      if (i == 2) sym_key();
  if (i == 3) sym_flame();     if (i == 4) sym_star();      if (i == 5) sym_wave();
  if (i == 6) sym_mountain();  if (i == 7) sym_hourglass(); if (i == 8) sym_tree();
  if (i == 9) sym_compass();   if (i == 10) sym_diamond();  if (i == 11) sym_eye();
}

// ------------------------------------------------------------------ plate ---
W = 2*margin + 11*pitch + 8 + 6;           // extra 6 mm on the left for the row dots
D = 2*margin + (len(rows) - 1)*row_pitch + 8;
function sx(i) = margin + 6 + 4 + i*pitch;
function sy(r) = D - margin - 4 - r*row_pitch;

module symbols3d(kind) for (r = [0:len(rows) - 1]) if (rows[r][0] == kind)
  for (i = [0:11]) translate([sx(i), sy(r), plate_t - rows[r][2]])
    linear_extrude(rows[r][2] + (kind == "recess" ? 1 : 0)) symbol(i, rows[r][1]);

module body() difference() {
  hull() for (x = [2, W - 2], y = [2, D - 2]) translate([x, y, 0]) cylinder(r = 2, h = plate_t);
  symbols3d("inlay");                       // cavities, filled by the inlay part
  symbols3d("recess");                      // open recesses for paint-fill
  for (r = [0:len(rows) - 1]) for (k = [0:r])   // row dots
    translate([margin + k*1.8 - (r*0.9) + 2.2, sy(r), plate_t - 0.4]) cylinder(d = 1.1, h = 1, $fn = 12);
}
module inlay() {
  symbols3d("inlay");
  for (r = [0:len(rows) - 1]) if (rows[r][0] == "raised")      // stand proud of the plate
    for (i = [0:11]) translate([sx(i), sy(r), plate_t - eps]) linear_extrude(rows[r][2] + eps) symbol(i, rows[r][1]);
}

if (part == "body") body();
if (part == "inlay") inlay();
if (part == "preview") { color([0.90, 0.87, 0.78]) body(); color([0.1, 0.1, 0.1]) inlay(); }
