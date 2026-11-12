#!/usr/bin/env bash
# Exports every printable part to stl/, renders the views to images/, and runs
# the interference checks.   Usage: ./build.sh [stl|img|check|all]   (default all)
# Extra OpenSCAD overrides can be passed via SCAD_ARGS, e.g.
#   SCAD_ARGS="-D uv_d=16 -D uv_len=58" ./build.sh stl
set -u
cd "$(dirname "$0")"
SRC=cad/chronometer.scad
MODE=${1:-all}
SCAD_ARGS=${SCAD_ARGS:-}
mkdir -p stl images build
OSC="openscad"
command -v xvfb-run >/dev/null && [ -z "${DISPLAY:-}" ] && OSC="xvfb-run -a openscad"

PARTS="base test_base deck outer_ring inner_ring index_cap pawl_outer pawl_inner cover keystone mask uv_ring door fragment_1 fragment_2 fragment_3 fragment_4 plate_small_parts plate_fragments"
EMPTY_CHECKS="chk_rings_deck chk_rings_cap chk_rings_cover chk_cover_deck chk_cover_base chk_cover_insert chk_pawls_deck chk_pawls_cap chk_door_base chk_mask_base chk_frag_cover chk_frag_knob chk_frag_frag"
NONEMPTY_CHECKS="chk_keying chk_detent"

run() { # name, outfile
  $OSC -o "$2" -D "part=\"$1\"" $SCAD_ARGS "$SRC" >"build/$1.log" 2>&1
}

if [ "$MODE" = stl ] || [ "$MODE" = all ]; then
  echo "== STL export"
  for p in $PARTS; do
    ( run "$p" "stl/$p.stl" && echo "  ok   $p" || { echo "  FAIL $p"; tail -3 "build/$p.log"; } ) &
    while [ "$(jobs -r | wc -l)" -ge 4 ]; do sleep 0.3; done
  done
  wait
fi

if [ "$MODE" = check ] || [ "$MODE" = all ]; then
  echo "== Interference checks (parts in assembled position)"
  for c in $EMPTY_CHECKS $NONEMPTY_CHECKS; do
    ( run "$c" "build/$c.stl"
      # "empty" = no geometry, or only zero-volume contact faces (< 0.05 mm^3)
      if grep -q "top level object is empty" "build/$c.log"; then r=empty
      elif python3 scripts/stl_info.py --volume-below 0.05 "build/$c.stl"; then r=empty; else r=solid; fi
      case " $EMPTY_CHECKS " in
        *" $c "*) [ $r = empty ] && echo "  pass $c (no overlap)" || echo "  FAIL $c (parts overlap)";;
        *)        [ $r = solid ] && echo "  pass $c (overlap expected)" || echo "  FAIL $c (expected overlap missing)";;
      esac ) &
    while [ "$(jobs -r | wc -l)" -ge 4 ]; do sleep 0.3; done
  done
  wait
fi

if [ "$MODE" = img ] || [ "$MODE" = all ]; then
  echo "== Renders"
  img() { # part, file, camera
    $OSC -o "images/$2" -D "part=\"$1\"" $SCAD_ARGS --imgsize=1600,1200 --camera="$3" \
      --colorscheme=Tomorrow "$SRC" >"build/img_$2.log" 2>&1 && echo "  ok   $2" || echo "  FAIL $2"
  }
  img assembly assembly.png      "0,0,14,52,0,20,360" &
  img assembly back.png          "0,0,14,215,0,200,360" &
  img section  section.png       "0,0,14,68,0,90,300" &
  img exploded exploded.png      "0,0,60,68,0,25,560" &
  wait
fi
