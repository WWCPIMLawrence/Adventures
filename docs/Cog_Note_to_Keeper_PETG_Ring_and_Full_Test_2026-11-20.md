# Cog to Keeper: PETG retaining ring, full-assembly test kit (20 Nov 2026)
CAD statements are predictions; no physical result is claimed.

## 1. Can the PETG retaining ring be eliminated safely? (your item 4)
**Mechanical implications: none found, from reading the CAD.** In the plain/gate configuration (latch off) the ring's only job is to hold the paper UV disc inside the cover skirt (its latch nubs and slots are disabled). The push-and-turn mechanism involves only the cover's lugs and flange, the deck's bay tracks and gate pockets, and the six PETG strips: `chk_gate_up`, `chk_gate_blocked`, `chk_gate_pressed`, `chk_gate_pressed_path` and `chk_bow_*` contain the cover, deck and strips and **do not include the ring**. The cover's inner ledge (ring_ledge) stays in the cover and becomes unused; **no cover geometry is changed**. The ring occupied the outer part of the cover underside (r 19.4 to 23.3 mm), so omitting it also leaves the underside clear for the UV writing.
**Not changed; no production revision made.** Proposed: run the full-assembly test **without** the ring, so the test itself proves it; if anything differs (cover rattle, play), the ring can be fitted back. The strips-hold-the-keeper-ring effect the owner saw is the stand-in ring and is unrelated.

## 2. Full-assembly kit (your item 1)
`downloads/gate_T1-v1_full_assembly_kit.zip`: `deck_T1-v1.stl` (one print, alone on the bed, 125 x 125 x 5 mm, 25.5 cm3) and `PRINT_AND_TEST_T1-v1_FULL_ASSEMBLY.txt`. CAD checks pass (strips slide in, the inner ring clears the strips, gate holds and releases). **Build-order warning, written into the test sheet: the strips go in before the inner ring**, because the ring closes the open ends of the slots. The test uses the owner's existing base, rings, index cap with three M3 x 16 screws, pawls, fragments, the T1-v1 cover and strips, and an M3 x 12 knob screw; the sheet says "say so if a part is missing, do not substitute". Pawl, screw and knob counts are still unconfirmed. Whether the three existing latch decks are usable instead is unverified and is not part of this test.

## 3. M3 x 12 knob screw (item 2), CAD arithmetic
Fragment lift about 2.6 mm (about 5 turns). M3 x 12: 2.3 mm of shank spare beyond the nut at that lift; it leaves the nut after 7.3 mm; tip 3.1 mm below the cover's flange underside (inside the well). M3 x 14 only if the owner finds 12 short. The sheet records turns, engagement, fragment clearance and underside interference.

## 4. UV writing and strips (items 3 and 5)
Direct UV handwriting on the cover underside (SUN TO ARROW, three lines, clear of the centre) is built into the test steps; the sheet checks legibility under UV and invisibility in normal light after the cycles. The 0.7 mm strips stay; no tolerance change was made.

Not four-unit production approval. Hard stop Sun 22 Nov.
