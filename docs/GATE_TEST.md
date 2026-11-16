# Push-and-turn gate and ring ledge - test variant (prototype, not production)

Full write-up with figures: `docs/Chronometer_gate_test_handoff.pdf`. Print guide and the seven tests: the zip's `PRINT_GUIDE.txt`.

**Production is unchanged.** Every option below defaults off; all 30 default part exports match the previous ones in volume and
bounding box, and the 27 existing interference checks pass.

| Option (cad/chronometer.scad) | Default | Variant used for the test |
|---|---|---|
| `gate_on` | false | true: lug pockets 0.9 mm higher, vertical wall, six bow-spring pockets in the hub |
| `latch_on` | true | false: no nubs, no cover slots, no deck grooves, plain split ring with pinch tabs |
| `ring_retain` | "bumps" | "ledge": flat-faced ledge under the ring |
| `cover_rim` | "knurl" | "smooth" |

Build and check the variant: `scripts/gate_check.sh` (exports `build/test_gate/`, runs 9 gate checks and 12 stack checks).
Numbers: `scripts/gate_numbers.py`. Figure: `scripts/gate_figure.py`. Test STLs: `stl/test/gate/`.

Parts that change in the variant: deck (seat), cover, ring, plus six printed bow springs. Nothing else.
