# Cog to Keeper: captured-strip gate T1-v1, model, checks and test kit (19 Nov 2026)
All figures here are CAD predictions or beam-theory estimates unless marked PHYS. Nothing has been printed yet. Hard stop: Sun 22 Nov. No other mechanical redesign is being started.

## What was built (variant switch `bow_tslot=true`, default off: default geometry unchanged, same volume and bounding box)
- Each strip foot gets an **inward hook** (0.8 mm reach, 0.5 mm high) at the bottom. The deck has a matching cavity under a 0.98 mm ledge. The channel for each strip **opens through the hub's outer face**, so a strip slides in radially from outside and cannot be pulled straight up. The strips lie in the print plane (printed on their side), so the hooks need no supports.
- The **inner ring**, fitted over the hub afterwards, closes the open ends. Scripts: `scripts/tslot_check.sh`; CAD in `cad/chronometer.scad` (parameters `bow_tslot`, `bow_hook_ov`, `bow_hook_h`, `bow_hclr`, `bow_out_ext`).

## Your five pre-print items
1. **Model and validate:** done, all pass (below).
2. **Inner ring retains the strips without interfering with ring rotation:** a seated strip's corners reach r 27.84; the ring's journal surface is r 28.3, so 0.46 mm clear (`chk_tslot_ring_clear` EMPTY from 0 to 0.45 mm of outward drift); a strip pushed out 0.6 mm hits the ring (`chk_tslot_ring_stop` NON-EMPTY, it cannot leave; its feet stay in their slots). **Residual risk:** nothing holds a strip against drifting outward up to 0.47 mm, at which point a corner could rub the rotating ring. No fix is proposed without approval; the test should note any ring drag.
3. **PETG clearances, installation, stress:** hook clearance 0.12 mm per side, foot slot 0.07 mm per side (as before); installation is a straight radial slide, no flexing (`chk_tslot_slide` EMPTY along the path). Arch strain about 2 % in use (as before; PETG, lower-bound beam model). Hook yield load about 5.8 N each (PETG in-layer 40 MPa, hook root bending), against a strip weight pull of about 0.002 N; the ledge is deck PLA with more capacity. Press force predicted 8.4 N for the 0.7 mm strip, 12.5 N for 0.8 mm (estimates, measured PETG stiffness unknown). **Risk:** print tolerance on 0.12 mm clearances. If strips bind, the owner is told not to force them.
4. **Reconciled against the spring crown:** the T-slot variant keeps the six separate strips and the existing deck bayonet and pockets, and adds hooks and an outward channel; the spring crown needed a new deck groove, a new one-piece part and a retention concept of its own (also unproven). The T-slot concept is the smaller change. The crown is shelved; not designed further.
5. **Test kit and print list:** `downloads/gate_T1-v1_test_kit.zip` with `PRINT_AND_TEST_T1-v1.txt`: cover_T1-v1 (gate cover), seat_T1-v1, strips_T1-v1_soft07 (PETG), keeper_ring_T1-v1 (stand-in for the inner ring), optional strips_T1-v1_firm08. Reuse the PETG ring (same part as ring_O2-v1). Version-marked on the part with a marker.

## CAD checks (all pass; predictions only)
- Empty as required: `chk_tslot_slide`, `chk_tslot_seated`, `chk_tslot_ring_clear`, `chk_gate_up`, `chk_gate_pressed`, `chk_gate_pressed_path`, `chk_bow_deck`, `chk_bow_cover`, `chk_ring_ledge`, `chk_cover_deck`, `chk_cover_base`, `chk_cover_insert`, `chk_cover_path`, `chk_rings_cover`, `chk_rings_deck`, `chk_knob_cover`, `chk_frag_cover`.
- Solid as required: `chk_tslot_lift` (a lifted strip is caught by the hook), `chk_tslot_ring_stop`, `chk_gate_blocked` (cover cannot turn the unlocking way unless pressed), `chk_bow_proud`, `chk_ring_ledge_hold`.

## Physical acceptance (as you specified; owner)
Strips stay in over 10 cover removals and a shake; zero and four fragments, 10 knob remove/install cycles each; the same with pressure on the knob; normal handling with the cover staying attached; deliberate press-and-turn opening 10 of 10.

## Notes
- The owner proposed two further concepts (a mid-travel exit with a locked stop on each side, and a left-hand-thread screw-on cover). **Not pursued**, per your rule against another mechanical redesign without your approval. Listed for your information only; Cog thinks the mid-travel exit is worth considering if T1-v1 fails.
- Not touched: the integrated aperture, fragment geometry, keyed lid, M-72.
- Known limit: this test seat uses a stand-in keeper ring, not the real inner ring. The real ring/strip interaction is checked in CAD only until a full assembly is built.
