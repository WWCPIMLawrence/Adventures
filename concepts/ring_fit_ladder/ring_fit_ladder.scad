// NON-PRODUCTION diagnostic: four thin rings with different bores to find what really fits the printed hub (nominal hub OD 56.0 mm).
// Bore 56.6 is the real inner ring's design bore; the others open it up. Outer rim notches tell them apart (0 to 3 notches).
bores = [56.6, 56.8, 57.0, 57.2];
h = 3.0; wall = 3.0;
module ring(b, n) {
  difference() {
    union() { cylinder(d = b + 2*wall, h = h, $fn = 180); }
    translate([0, 0, -1]) cylinder(d = b, h = h + 2, $fn = 180);
    for (k = [0:n - 1]) rotate([0, 0, 40*k]) translate([b/2 + wall + 0.3, 0, -1]) cylinder(d = 1.6, h = h + 2, $fn = 20);
  }
}
for (i = [0:3]) translate([(i % 2)*70, floor(i/2)*70, 0]) ring(bores[i], i);
