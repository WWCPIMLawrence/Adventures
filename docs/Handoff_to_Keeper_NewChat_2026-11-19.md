# The Timekeeper's Paradox: Chronometer, handoff to a new Keeper chat
**Date:** Thursday 19 November 2026 (evening)   **From:** Cog (Claude Code: CAD, validation design, production files)   **To:** Keeper (ChatGPT Planning), new chat
**Hunt: Sunday 29 Nov 2026. Packing: Saturday 28 Nov evening.** Whether the earlier "preparation complete Wed 25 Nov" date moved with the hunt is **unconfirmed** (ask the owner).
This file adds to, and where they disagree replaces, `Chronometer_Full_Status_Handoff_2026-11-17.md` (the full project description, settled puzzle facts, aperture coordinates and old production plan). Read that for background; **this one is the current state.** Physical results are the owner's; CAD figures are Cog's predictions and are labelled.

## 1. Roles and standing rules
- **Keeper** decides. **Scribe** (ChatGPT Work) writes puzzle papers and the journal leaf. **Cog** does CAD, checks and production files. The **owner** prints, assembles and tests, and relays between the three.
- No change to approved production geometry or the frozen aperture coordinates without explicit approval. Report CAD predictions separately from physical results; never present a computed result as a physical pass. Tell the owner exactly which parts to print. Do not assume inventory. Flashlight stays a hidden surprise; the 2.5 mm Allen key is a clue-envelope reward, not a compartment.
- Process lesson from this week: the owner printed many centre-cover variants, cannot say which version is in the prototype, and wasted filament and time. **From now on every test part is version-marked** (file name plus a marker pen note on the part), old parts go in a box marked OLD, and Cog gives the owner one short print list at a time.

## 2. Your decision of 19 Nov, and where it stands
You chose **Option 2: plain retaining ring with the flat ledge, gate retired if it passes**, and required the knob test on a version-marked assembly before production approval; no keyed-lid work; M-72 paper overlay may continue if it does not delay production.
- **Test kit O2-v1 built** (Cog, CAD checks pass; those are predictions only): `cover_O2-v1`, `ring_O2-v1` (PETG), `seat_O2-v1`, with a one-page test sheet. Parameters: gate off, latch off, ring_retain "ledge", smooth cover rim. Script `scripts/option2_check.sh`.
- **The owner is printing it tonight** (cover and seat first, about 37 min, then the PETG ring). The test is yours: A zero fragments, unscrew and reinstall the knob 10 times; B same with four fragments; check the cover does not rotate, lift or detach; C deliberate anticlockwise opening works (5 times); D ring does not snag or fall out. **Result expected Fri 20 Nov; nothing is known yet.**
- **If it passes:** Cog reports it; you approve Option 2 and retire the gate. **If it fails:** Cog reports the exact failure *before* changing CAD, then one version-marked spring-crown test kit with a hard deadline (Cog suggested Sun 22 Nov, then fall back).
- Unchecked by Cog: the owner's three existing decks are **latch decks** (they have nub grooves in the well wall). With a no-nub Option 2 cover they are probably still usable (the grooves are extra voids; the cover rides the bayonet tracks) but this has **not been verified**. Cog will check in CAD, otherwise four new plain decks are needed.

## 3. What happened with the gate (physical, owner-reported)
- Push-and-turn feel was validated earlier. But the **printed PETG bow strips repeatedly fell out of the hub when the cover was removed** (two sets, 8 and then a similar set, photographed loose beside the hub). The centre also "falls out after one twist" on the prototype, and the owner cannot say which hub version it has. The knob test was never run.
- **Cause (CAD, read from source):** each strip foot sits in a slot 0.07 mm wider per side than the foot (`bow_fit`; Cog's comment called it a press fit, it is a clearance); nothing holds a foot down once the cover lifts. Stiffer strips (0.9, 1.0 mm, prepared in `concepts/gate_contingency/`) do not fix it; glue is not acceptable for repeated player handling; a snap-barb foot would strain PETG about 18 % (estimate). The only credible gate fix is a one-piece spring crown plus a new deck, unproven until printed. Hence Option 2.
- The old three-arm latch is **not a fallback** (it fails: knob loosening drags the cover, ring snags).
- The gate decision note sent to you: `Cog_Note_to_Keeper_Gate_Decision_2026-11-19.md`.

## 4. Inventory (owner-reported 18 to 19 Nov; verify, Cog does not assume)
- Printed and usable: **3 back plates** with the integral aperture, **4 bases**, **3 decks (latch type)**, **3 inner rings**, **3 index caps**; **1 good bone outer ring**; the **fully assembled prototype** (its outer ring is white, not bone). A second bone outer ring is scrap (printed beside a failed inner ring).
- **Tiles: only one set exists, in the prototype; four are needed.** Covers, strips and pawls: unknown or not production-ready. Filament, screws (M3x8, M3x16, M3x10 knob), nuts, hex keys, flashlights: unknown. Screw-head dimensions and the Phillips knob screw size: not supplied (keystone pocket held).
- **Prototype as emergency spare:** only if it passes the same functional tests (knob test, registration, ring).

## 5. Other threads
- **Outer ring quality.** A white-lettered ring (white filament) and two bone rings were printed; one bone ring came out soft (partly from a failed inner ring on the same bed). Cog reviewed the owner's Bambu Studio profile "Chronometer" and suggested, for outer rings only (separate profile, so the tuned fit settings stay for cover and seat): outer-wall speed 200 to about 100, inner wall 300 to about 150, inner-wall acceleration 0 (falls back to 10000) to about 2500, outer wall 5000 to about 2500, small-perimeter 100 %, detect thin wall on. Possible grey lettering from too small a purge volume is **unconfirmed**; Cog still needs the **purging-volume table and filament settings** (flow ratio, pressure advance, temperature, volumetric speed). Four matching outer rings are needed; one good bone ring exists. The owner is printing two bone outer rings overnight (instruction: rings only on that bed).
- **Registration / compositor proof.** CAD: the black outer ring covers the fixed notch from directly above (visible groove height is about 14.2 x cos(elevation): 0 mm at 90 degrees, 4.9 mm at 70, 7.1 at 60, 9.1 at 50). **Physical test with the real proof from above and at normal handling angles is required** before accepting side-view notch alignment; if players cannot align from above, a printed top-view mark is a Keeper/Scribe decision. The real journal leaf has **not been received by Cog**; Scribe's files must be attached.
- **M-72 attachment (nonproduction).** Paper overlay test with windows p4/p6/p8 and p4/p8/p10 (both templates built, `m72_paper_overlay_template*_NONPRODUCTION.pdf`). CAD: both arrangements give 144 distinct signatures and 22 wrong settings show 3 of 6 correct glyphs; p4/p8/p10 hides DIAMOND at correct calibration and shows SUN and KEY (a story decision). **Not yet run by the owner.** No rigid plate authorised; one proof print could follow a good paper test.
- **Music House keyed lid (nonproduction).** Parked, as you directed. Existing plates cannot be retrofitted; five replacement plates are not authorised. Prototype files exist in `concepts/music_house_shutter/` (coupon, two lids, long key, fit checks) and are **not** to be printed unless you reopen it.
- **Not yet received by Cog:** Scribe's journal leaf and its test PDF; owner's knob-test results; paper overlay result; screw-head measurements.

## 6. What Cog is waiting for and proposes next
1. O2-v1 knob-test result (Fri 20 Nov). Then production approval or a failure report.
2. If it passes: freeze Option 2 files; production list per instrument = base, back plate, deck, cover (smooth rim), PETG plain ring, outer ring, inner ring, index cap, keystone knob, four tiles, pawls. No strips. Cog will confirm whether the three latch decks are usable.
3. Pilot instrument first, then the real journal proof read in both orders (Mon 23 as before), then tests and reprints, packing Sat 28.
4. The gate-specific clue ("press the dial in and turn it back") **is no longer needed** under Option 2; Scribe should drop it and use a plain "turn the centre cover anticlockwise to open" style instruction. (Confirm after the test.)

## 7. Decisions and answers needed from you
1. Confirm the production deadline (does Wed 25 still stand or has it moved to Fri 27/Sat 28?).
2. Is the smooth cover rim approved (owner feedback pending)?
3. Ask Scribe for the journal leaf and test PDF, and relay them to the owner to attach for Cog.
4. Who supplies and prints tiles (four sets) and what is the filament stock?
5. If O2-v1 fails: approve one spring-crown kit with the 22 Nov stop date, or choose another retention concept.

## 8. Files (repository `WWCPIMLawrence/2026---Chronometer-`, branch `claude/brave-ramanujan-dc57dr`; `downloads/` holds copies)
`downloads/option2_test_kit_O2-v1.zip`; `PRINT_AND_TEST_O2-v1.txt`; `Cog_Note_to_Keeper_Gate_Decision_2026-11-19.md`; `Test_Packet_Nov19-22_and_Response_to_Keeper_2026-11-19.md`; `Cog_Update_to_Keeper_2026-11-19.md`; `Engineering_Report_to_Planning_2026-11-18.md`; `M72_*`, `MusicHouse_Keyed_Shutter_Feasibility_2026-11-18.md`; `PRINT_QUEUE_2026-11-18.md`, `PRINT_CHECKLIST.md`; combined `ALL_LATEST_2026-11-17.zip`. Raw GitHub base: `https://raw.githubusercontent.com/WWCPIMLawrence/2026---Chronometer-/claude/brave-ramanujan-dc57dr/downloads/`. Frozen aperture: `reference/aperture_geometry.json` (SHA-256 `a37d539b04742708671a6f8608ef5e3975aca82f4068ecf44af8edda2a374aa8`).
