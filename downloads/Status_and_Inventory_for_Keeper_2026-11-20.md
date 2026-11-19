# Chronometer: current status and printed inventory, for Keeper (Fri 20 Nov 2026, morning)
From Cog (Claude Code) via the owner. Read after `Handoff_to_Keeper_NewChat_2026-11-19.md` and `Cog_Report_to_Keeper_T1-v1_Model_and_Checks_2026-11-19.md`. **Counts below are the owner's reports (18 to 20 Nov); Cog has not verified them and does not assume anything not listed.** CAD figures are predictions; PHYS = reported by the owner.

## 1. Where things stand
- **Hunt Sun 29 Nov; packing Sat 28 Nov.** Whether the earlier "preparation complete Wed 25" date moved is still unconfirmed.
- **Centre cover (the critical path).** Option 2 (plain ring) was rejected: nothing resists turning (PHYS: a tiny anticlockwise twist releases it; the knob test was not run). You approved **T1-v1** (captured-strip push-and-turn gate) for one physical test, with the hard stop **Sun 22 Nov** and no other mechanical redesign without your approval. The CAD checks all pass (predictions only). **Not printed or tested yet.**
  - **Today:** the owner is printing the PLA parts (cover, seat, keeper ring) before work; the PETG strips are printed this evening, then the test assembly and test run per `PRINT_AND_TEST_T1-v1.txt`. Result expected tonight or this weekend.
  - A pass with the stand-in ring is preliminary: production approval needs the real inner ring and knob, which means a full gate deck and a base. Cog prepares that deck only if the stand-in test passes.
- **Integrated aperture back plate:** validated by the owner on a printed plate (holes 10.5 and 2.5 mm, flat, template matches). **Not yet tested with the real journal leaf**, which Cog has not received from Scribe.
- **Outer rings:** two bone outer rings printed overnight; the owner reports they "look great" (PHYS; which slicer settings were used is not confirmed).
- **Not tested yet:** the compositor proof from above and at handling angles (the black outer ring hides the fixed notch from directly above, CAD); the M-72 paper overlay (both templates ready, owner has not run them); the knob test; keystone knob screw-head pocket (held for the Phillips/screw-head measurements).
- **Parked, not authorised:** keyed lid, M-72 production attachment, spring crown, mid-travel exit, left-hand-thread cover.

## 2. Printed inventory (owner-reported) against four instruments
| Part | Have (usable, as reported) | Need for 4 | Short / notes |
|---|---|---|---|
| Bases | 4 | 4 | complete (owner confirmed the right version by its marks) |
| Back plates with integral aperture | 3 | 4 | **1 short** (plus a spare if capacity) |
| Decks | 3 **latch** decks | 4 **gate** decks (if the gate is approved) | the 3 existing decks are latch decks: probably not usable with a gate; **4 new decks needed** if the gate passes |
| Centre covers (production) | 0 | 4 | only test variants exist (many old ones, plus O2-v1 and T1-v1 test parts); production covers wait for the test |
| Retaining rings (PETG) | 1 (O2-v1 ring) | 4 | the ring is the same part for the gate; 3 more needed |
| Gate strips (PETG) | none usable (old strips fell out) | 24 (6 per instrument) plus spares | T1-v1 strips print this evening (test only) |
| Outer rings, bone | 3 (1 earlier plus 2 overnight) | 4 | **1 short**; the white-ringed prototype ring is not matching |
| Inner rings | 3 | 4 | **1 short**; one failed inner-ring print was scrapped |
| Index caps | 3 | 4 | **1 short** |
| Keystone knobs | unknown | 4 | held for the screw measurements |
| Fragment tile sets | 1 (in the prototype) | 4 | **3 short** |
| Pawls (PETG, 4 per instrument) | unknown | 16 | owner to count |
| Screws, nuts, hex keys, flashlights, filament | unknown | see plan | owner to inventory |
**Also:** one fully assembled prototype (white outer ring, older centre). It is an **emergency spare only if it passes the same functional tests**. A second outer ring in bone that came out soft (printed beside a failed inner ring) is scrap. All old centre parts are boxed as OLD.

## 3. Remaining print work (what is not affected by the centre decision)
Back plate (1 plus spare), outer ring (1), inner ring (1), index cap (1), three tile sets, pawls (count), keystones (after screw size), small hardware. **Gate-dependent:** four gate decks, four covers, three more PETG rings, 24 strips plus spares (decks and covers only after the T1-v1 result).
Capacity: one P1S, one weekday job before work and evenings and weekends; the owner has lost two evenings this week to failed prints. Keeper's instruction to protect printer time for four working instruments is being followed.

## 4. Print settings and lessons (so they are not repeated)
- Plate: BIQU CryoGrip Pro Frostbite (soap and water only; slicer plate label may still say Bambu SuperTack, check it). First-layer adhesion failures were a dirty plate, not the files.
- Never share a bed with a part that might fail (a failed inner ring spoiled an outer ring beside it). Every test part is version-marked (file name plus marker pen); old centre parts are in the OLD box.
- Suggested for outer rings only (separate profile): outer wall 200 to about 100 mm/s, inner wall 300 to about 150, accelerations about 2500, small perimeters 100 %, detect thin wall on. The profile "Chronometer" (wall order outer/inner, elephant foot 0.15) is tuned for the bayonet fit: do not change it for fit-critical parts.

## 5. What Cog needs, and decisions for you
1. T1-v1 result (owner, tonight or weekend). Then: report to you before anything else changes.
2. The real preparation deadline; whether the smooth cover rim is approved.
3. Scribe's journal leaf and test PDF, attached by the owner, for the real-sheet test of the aperture plate.
4. Tile sets: who prints three more, and filament stock; screw-head size for the keystone pocket.
5. If T1-v1 fails: your choice of the next step. Cog had flagged the mid-travel exit as the leading alternative, but will not pursue it without your authorisation.

## 6. Files
Repository `WWCPIMLawrence/2026---Chronometer-`, branch `claude/brave-ramanujan-dc57dr`; `downloads/` includes `gate_T1-v1_test_kit.zip`, `PRINT_AND_TEST_T1-v1.txt`, the reports named above, and `ALL_LATEST_2026-11-17.zip` (everything). Raw base: `https://raw.githubusercontent.com/WWCPIMLawrence/2026---Chronometer-/claude/brave-ramanujan-dc57dr/downloads/`.
