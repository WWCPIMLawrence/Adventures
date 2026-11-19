#!/usr/bin/env bash
# Captured-strip (hook) gate variant, Keeper-approved test only (19 Nov): exports the test parts and runs the checks.
# CAD checks are predictions, not physical results.
set -u; cd "$(dirname "$0")/.."
SRC=cad/chronometer.scad; OSC="openscad"; command -v xvfb-run >/dev/null && [ -z "${DISPLAY:-}" ] && OSC="xvfb-run -a openscad"
V='-D gate_on=true -D latch_on=false -D ring_retain="ledge" -D cover_rim="smooth" -D bow_tslot=true'
OUT=${1:-build/tslot}; mkdir -p "$OUT"
exp() { eval $OSC -o "$OUT/$2" -D "'part=\"$1\"'" $V $3 "$SRC" >"$OUT/$1.log" 2>&1; }
chk() { eval $OSC -o $OUT/$1.stl -D "'part=\"$1\"'" $V "$SRC" >$OUT/$1.log 2>&1
  if grep -q "top level object is empty" $OUT/$1.log; then r=empty; elif python3 scripts/stl_info.py --volume-below 0.05 $OUT/$1.stl; then r=empty; else r=solid; fi
  [ $r = $2 ] && echo "  pass $1 ($2)" || echo "  FAIL $1 (got $r, wanted $2)"; }
if [ "${2:-all}" != check ]; then
  exp test_seat seat_T1-v1.stl "-D test_mark=0" & exp cover cover_T1-v1.stl "" & exp gate_bows strips_T1-v1_soft07.stl "-D bow_t=0.7" & exp gate_bows strips_T1-v1_firm08.stl "-D bow_t=0.8" & wait
  exp tslot_keeper keeper_ring_T1-v1.stl ""
fi
echo "== checks"
for c in chk_tslot_slide chk_tslot_ring_clear chk_tslot_seated chk_gate_up chk_gate_pressed chk_gate_pressed_path chk_bow_deck chk_bow_cover chk_ring_ledge; do chk $c empty & while [ "$(jobs -r | wc -l)" -ge 4 ]; do sleep 0.3; done; done; wait
for c in chk_tslot_lift chk_tslot_ring_stop chk_gate_blocked chk_bow_proud chk_ring_ledge_hold; do chk $c solid & while [ "$(jobs -r | wc -l)" -ge 4 ]; do sleep 0.3; done; done; wait
for c in chk_cover_deck chk_cover_base chk_cover_insert chk_cover_path chk_rings_cover chk_rings_deck chk_knob_cover chk_frag_cover; do chk $c empty & while [ "$(jobs -r | wc -l)" -ge 4 ]; do sleep 0.3; done; done; wait
python3 scripts/stl_info.py $OUT/*_T1-v1*.stl
