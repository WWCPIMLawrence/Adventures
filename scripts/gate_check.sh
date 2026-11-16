#!/usr/bin/env bash
# Push-and-turn gate variant: exports the test parts and runs the gate checks.
# Variant parameters: gate on, no sprung nubs, ledge for the ring, smooth cover rim.
set -u
cd "$(dirname "$0")/.."
SRC=cad/chronometer.scad
OSC="openscad"; command -v xvfb-run >/dev/null && [ -z "${DISPLAY:-}" ] && OSC="xvfb-run -a openscad"
V='-D gate_on=true -D latch_on=false -D ring_retain="ledge" -D cover_rim="smooth"'
OUT=build/test_gate; mkdir -p "$OUT"
exp() { eval $OSC -o "$2" -D "'part=\"$1\"'" $3 "$SRC" >"build/gate_$1.log" 2>&1; }
chk() { # name expect(empty|solid)
  eval $OSC -o build/gate_$1.stl -D "'part=\"$1\"'" $V "$SRC" >build/gate_$1.log 2>&1
  if grep -q "top level object is empty" build/gate_$1.log; then r=empty
  elif python3 scripts/stl_info.py --volume-below 0.05 build/gate_$1.stl; then r=empty; else r=solid; fi
  [ $r = $2 ] && echo "  pass $1 ($2)" || echo "  FAIL $1 (got $r, wanted $2)"; }
if [ "${1:-all}" != check ]; then
  echo "== export"
  exp test_seat "$OUT/test_seat_gate.stl" "$V" & exp cover "$OUT/cover_gate.stl" "$V" &
  exp uv_ring_plain "$OUT/uv_ring_plain.stl" "$V" & exp gate_bows "$OUT/gate_bows_soft.stl" "$V -D bow_t=0.7" &
  wait
  exp gate_bows "$OUT/gate_bows_firm.stl" "$V -D bow_t=0.8" &
  exp cover "$OUT/cover_latch_ledge.stl" "-D ring_retain=\"ledge\" -D cover_rim=\"smooth\"" &
  wait; ls -la "$OUT"
fi
echo "== gate checks"
for c in chk_gate_up chk_gate_pressed chk_gate_pressed_path chk_bow_deck chk_bow_cover chk_ring_ledge; do chk $c empty & done; wait
for c in chk_gate_blocked chk_bow_proud chk_ring_ledge_hold; do chk $c solid & done; wait
echo "== existing stack checks, gate variant"
for c in chk_rings_cover chk_cover_deck chk_cover_base chk_cover_insert chk_cover_path chk_cover_path_base chk_mask_base chk_mask_lip chk_frag_cover chk_knob_cover chk_rings_deck chk_rings_cap; do chk $c empty & while [ "$(jobs -r | wc -l)" -ge 4 ]; do sleep 0.3; done; done; wait
