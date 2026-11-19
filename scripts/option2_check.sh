#!/usr/bin/env bash
# Option 2 (Keeper decision 19 Nov): plain retaining ring with a positive flat ledge, no gate, no sprung nubs, smooth rim.
# Exports the version-marked test parts and runs the fit checks. Checks are CAD predictions, not physical results.
set -u; cd "$(dirname "$0")/.."
SRC=cad/chronometer.scad; OSC="openscad"; command -v xvfb-run >/dev/null && [ -z "${DISPLAY:-}" ] && OSC="xvfb-run -a openscad"
V='-D gate_on=false -D latch_on=false -D ring_retain="ledge" -D cover_rim="smooth"'
OUT=${1:-build/opt2}; mkdir -p "$OUT"
exp() { eval $OSC -o "$OUT/$2" -D "'part=\"$1\"'" $V "$SRC" >"$OUT/$1.log" 2>&1; }
chk() { eval $OSC -o $OUT/$1.stl -D "'part=\"$1\"'" $V "$SRC" >$OUT/$1.log 2>&1
  if grep -q "top level object is empty" $OUT/$1.log; then r=empty; elif python3 scripts/stl_info.py --volume-below 0.05 $OUT/$1.stl; then r=empty; else r=solid; fi
  [ $r = $2 ] && echo "  pass $1 ($2)" || echo "  FAIL $1 (got $r, wanted $2)"; }
exp cover cover_O2-v1.stl & exp uv_ring_plain ring_O2-v1.stl & exp test_seat seat_O2-v1.stl & wait
for c in chk_ring_ledge chk_cover_deck chk_cover_base chk_cover_insert chk_cover_path chk_rings_cover chk_knob_cover chk_frag_cover; do chk $c empty & while [ "$(jobs -r | wc -l)" -ge 4 ]; do sleep 0.3; done; done; wait
chk chk_ring_ledge_hold solid
python3 scripts/stl_info.py $OUT/*_O2-v1.stl
