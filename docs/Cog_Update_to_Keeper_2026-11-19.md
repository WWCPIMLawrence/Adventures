# Cog (Claude Code, Chronometer engineering): update to Keeper

**Date:** 18 to 19 Nov 2026 (Wednesday night).  **Hunt:** Sunday 29 Nov; everything packed by Sat 28 evening.  **Names:** Keeper = Planning, Scribe = Work (puzzle creation), Cog = Chronometer engineering.
Reported = said by the owner. Computed = from the CAD or scripts. **Nothing computed is a physical pass.** Nothing below has been changed in the approved production CAD since the integral-aperture default (commit `78419df` and later are documentation and nonproduction concepts only).

## 1. Answers to what Keeper asked
| Request | Where it stands | File |
|---|---|---|
| Re-plan the 3D-print queue around evening, overnight and before-work printing | **Done.** Three slots per workday, job list, calendar, unattended-run checklist. Shrunk after the owner's inventory (about 8 beds, about 10 h) | `PRINT_QUEUE_2026-11-18.md`, `PRINT_CHECKLIST.md` |
| M-72 removable calibration attachment (feasibility) | **Done.** Ranked: rigid sight plate, tested first as a paper overlay; keyed to the three fixed cap-screw heads; real two-ring dependency | `M72_Attachment_Feasibility_2026-11-18.md` |
| M-72 sight plate: the eight questions and physical test results | **Computed answers done; physical results NOT available** (Cog has no printer, paper or instrument). The paper proof is the owner's to run: test sheet written | `M72_Sight_Plate_Evaluation_and_Paper_Test_2026-11-18.md` |
| Music House keyed aperture shutter (feasibility) | **Done. Recommendation: simplify** (details below) | `MusicHouse_Keyed_Shutter_Feasibility_2026-11-18.md` |
| Review the unified handoff and report discrepancies | **Done** (`Engineering_Report_to_Planning_2026-11-18.md`) | |

## 2. M-72 sight plate: what to know
- **Concept:** a flat plate (paper or rigid printed) seats on the three index-cap screw heads (the only fixed, raised, uneven features: 5.5 mm heads at r 45, 25 / 150 / 270 deg). It seats in exactly one orientation (within 0.5 deg); a 120 deg turn misses by 3.9 mm. Windows A, B, C at p4, p6, p8 clockwise of the fixed arrow; outer XII / inner STAR calibration preserved; nothing depends on XII being zero.
- **A defect in my own first concept was found and fixed:** the 12 mm windows were narrower than the widest numeral (VIII is 12.6 mm wide, 8.2 mm tall). Windows are now 16.0 x 10.6 mm (numerals) and 10.0 x 9.3 mm (symbols), sized from the measured glyphs; a small window keeps the fixed arrow visible; all fit checks pass; the paper template was regenerated (same filename).
- **Signature (computed):** at the calibrated state A = IV / TREE, B = VI / DIAMOND, C = VIII / SUN. All 144 ring settings give 144 different six-glyph signatures. Any one window identifies both rings. A one-ring error shows exactly 3 of the 6 correct glyphs (22 such near-miss states). Full table for Scribe: `m72_signature_table_all144.csv`.
- **For Scribe to decide:** window B shows DIAMOND at the calibrated state (on the ring itself). If that is unwanted, choose other windows (for example p4, p8, p10). Build decoy records from real single-ring errors, and avoid decoys that evidence already collected (STAR 9:03, HOURGLASS 10:26) would rule out.
- **Parallax, rigid plate (computed worst case, visible fraction of a glyph at 0 / 15 / 25 / 35 deg):** square edges 100 / 93 / 85 / 74 %; with a 1 mm chamfer 100 / 95 / 90 / 83 %. Paper stays above 98 % to 35 deg.
- **Rings and cover:** the paper lies on the ribs, so calibrate first, then apply. The rigid plate hovers 0.8 mm above the tallest ring feature, so the rings turn with it on. No conflict with the cover (also lifted 1.2 mm by the gate) or with the keyed lid (no overlap).
- **Screw heads:** modelled at the ISO 4762 maximum (5.5 x 3.0 mm). **Not yet measured on the real instrument.**
- **Rigid plate worth printing? Conditionally yes, not yet approved.** About 17 cm3 and about 40 min each (two per bed); 4 plus a spare is about 3.5 h. Print only if the paper test shows 9 of 10 first-try seats, readable glyphs at 25 deg or less, and drag or tearing with paper (or Keeper wants a durable copy). Print one first.
- **Waiting on:** the owner's paper test (nine tests with a results table in the evaluation file).

## 3. Music House keyed shutter: what to know
- **Rejected on geometry: a captive rotating or sliding shutter.** The shutter must show the same four holes at "open"; **no rotation about the centre closes them**: the best angle (44 deg) still leaves 13 % of the open area uncovered. A slide needs 10.5 mm of travel and a 52 mm disc (the well is 50 mm). A swing needs a pivot about 85 mm away. The plate itself has only 0.8 mm of height to spare.
- **Feasible (computed): a keyed bayonet lid** that locks onto a **replacement** plate (three hooks standing in the well; the floor, holes and registration unchanged) and is turned about 32 deg and lifted with a **clock-winding key** (4 mm square tongue). Fit checks pass against the real assembly, including no overlap with the base, deck, cover and the M-72 plate. It blocks all four apertures from both sides and stays on the plate when the plate is removed.
- **Limits:** the key needs the cover removed first (the socket is at the bottom of the well; the 2.5 mm sighting hole is too small for the key); hooks are thin (0.55 mm) with a 1.4 mm overhang; radial clearances are only 0.25 to 0.3 mm; **no rotational detent yet**; it does not by itself give a reason to reassemble the instrument.
- **Existing plates cannot be retrofitted;** any retained cover needs reprinting the plates.
- **Recommendation: SIMPLIFY.** Hold the last plate prints (1 plus a spare) until a one-bed prototype (plate-centre coupon with hooks, one lid, one key; about 30 min of printing) passes on **Fri 20**. If it fails or time runs short, keep the validated plate and gate the discovery with the paper and the clue. If go: 5 plates (about 4 h), 5 lids and 5 keys (about 30 min) on Sun 22.

## 4. Current physical status (owner-reported unless stated)
- **Printed, not counting the assembled prototype:** 3 back plates (integral aperture), 4 bases, 3 decks (**latch decks, confirmed**: they have no spring pockets and cannot take the gate strips), 3 inner rings, 3 index caps, and 6 soft gate strips (PETG, version 2, printed tonight).
- **Prototype:** a nearly complete test unit; its outer ring is white, not bone; old centre cover; used for the centre-cover and knob tests; one tile set inside it. Not credited as one of the four.
- **Aperture plate:** validated on a printed plate (holes 10.5 and 2.5 mm, flat, bond holds, fits the base through repeated refits, 1:1 template matches). **Journal proof not yet tested.**
- **Centre cover:** the press-and-turn gate works in the owner's hands; **the knob test is not yet run**; the plain ring with ledge works. The old three-arm latch still fails the knob problem.
- **Remaining to print (about 8 beds, about 10 h):** outer rings x4 (none yet; the 2-hour job tonight was recommended, not confirmed), 1 inner ring, 1 index cap, 4 tile sets, 16 pawls and 4 plain rings (PETG), 4 covers, 4 keystones (held), 1 back plate plus a spare (held), decks (4 gate decks if the gate passes, else 1 latch deck), 24+ more strips if the gate is adopted.
- **Machine calibration:** two plates in 1:45 (about 53 min each); two 125 mm parts fit per bed.

## 5. Decisions needed from Keeper
1. **Keyed lid:** run the Fri 20 prototype, or skip it? Is a key that needs the cover removed first acceptable?
2. **If the gate fails the knob test:** (a) stiffer strips and retest, (b) latch with a "hold the disc while loosening the knob" clue and a spare, or (c) another mechanism (not currently planned). My preference: (a) then (b).
3. **M-72:** after the paper test, approve or decline the rigid plate. Confirm windows A, B, C at p4 / p6 / p8, or choose others (see the DIAMOND note).
4. **Journal registration:** the fixed notch is hidden from directly above by the uncut black outer ring (visible from the side or at an angle). Accept an oblique-view alignment? Suggested tolerance: RIFT centred within 1 mm, repeated after plate removal and refit.
5. **Spares policy** (plate, base, small parts) and whether the assembled prototype may serve as a spare unit despite the white outer ring.
6. **Cover release wording** for the host and the clues waits on the knob test: press down about 1 mm and turn anticlockwise (gate) or plain twist (latch).

## 6. Blocked or waiting on the owner
Knob test (0 and 4 tiles, hands-only, then with downward pressure); paper overlay test (T1 to T9); screw-head measurements; Phillips screw size (else the socket-head pocket stays); journal documents and host overlay (ChatGPT Library links cannot be opened by Cog: attach them); inventory of filament, screws, nuts, hex keys, lights; tile sets (4 needed).

## 7. Schedule (owner availability)
Wed 18 night: PETG parts, outer rings; knob test. Thu 19: decision gate or latch; freeze files; decks, covers. **Fri 20 (home all day): keyed-lid prototype, caps, rings, tiles.** Sun 22: production, assemble the pilot instrument. Mon 23 to Wed 25: morning plus overnight jobs, journal test with the real leaf, reprints. Thu 26: none. Fri 27: acceptance testing and repairs. Sat 28: final check and packing. Sun 29: cache placement, hunt.

## 8. Risks
No tested fallback if the gate fails; weekday printing limited to one before-work and one evening or overnight job; unmeasured numbers (gate press force, spring life, glare and opacity outdoors); the keyed lid and the rigid sight plate are both unprinted concepts; and any plate reprint competes for the same limited slots.

## 9. Files (repository `WWCPIMLawrence/2026---Chronometer-`, branch `claude/brave-ramanujan-dc57dr`)
Combined zip: `downloads/ALL_LATEST_2026-11-17.zip` (includes this update). Concepts and checks are under `concepts/` and are marked non-production.
