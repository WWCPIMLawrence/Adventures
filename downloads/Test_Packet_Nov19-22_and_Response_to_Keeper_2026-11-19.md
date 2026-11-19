# Cog: response to Engineering Review (18 Nov) and test packet for 19 to 22 Nov

Convention: **CAD** = computed or estimated by Cog. **PHYS** = filled in by the owner after a real test. Nothing in the CAD column is a physical pass. No production geometry changed; no optional part is authorised for full-scale manufacture.

## 1. Core mechanism first (priority 1)

**1A. Centre-cover knob test (decides gate vs latch).** Use the white-ring prototype, existing seat (`test_seat_gate.stl`), the soft PETG bows already printed.
Steps: hands only, 0 then 4 tiles, 10 cycles each direction; then repeat while pressing on the knob. Record: knob loosens cover? cover lifts when knob loosened? ring snags/falls? press-and-twist still releases?
| | CAD prediction | PHYS |
|---|---|---|
| Cover held against knob turning | gate pocket 0.9 mm deep stops rotation of cover under knob torque | |
| Press to release | 8 to 14 N (lower-bound beam model) | |
| Failure: cover lifts with knob | not predicted | |

**1B. If the gate fails: stiffer PETG strips, before any latch fallback.** Files `concepts/gate_contingency/gate_bows_t09_NONPRODUCTION.stl` (0.9 mm) and `..._t10_...` (1.0 mm). Current soft strip = 0.7 mm, firm = 0.8 mm (state which you printed).
Beam-theory table (PETG E 1900, six strips, simply supported; **a lower bound, real printed PETG stiffness is unknown**; treat as ratios):
| strip t (mm) | total stiffness N/mm | press to clear 1.05 mm | full 1.2 mm press | strain |
|---|---|---|---|---|
| 0.7 | 8.0 | 8.4 N | 9.6 N | 1.9 % |
| 0.8 | 11.9 | 12.5 N | 14.3 N | 2.0 % |
| 0.9 | 17.0 | 17.8 N | 20.4 N | 2.0 % |
| 1.0 | 23.3 | 24.4 N | 27.9 N | 2.0 % |
| 1.1 | 31.0 | 32.5 N | 37.2 N | 2.0 % |
Note: the pocket is 0.8 mm deep, so t above 0.8 sits 0.1 to 0.2 mm proud when flattened (accepted earlier). Strain about 2 % is high for PETG over many cycles; creep over a few days stored under load is unmeasured, so **store the instrument with the cover off the springs or test after 24 h compressed.** Print one set of each (about 5 min each, spare strips are cheap). Test in order 0.9, then 1.0. **Stop-rule:** 1.0 mm that is too hard to press comfortably (hand-fatigue, over about 25 N) is a fail, not a different problem.
**Old three-arm latch: not a fallback** unless its release procedure has been physically shown reliable (it currently fails: knob loosening drags the cover off, ring snags).

**1C. RIFT with the real journal leaf, including plate removal and refit.** Needs Scribe's journal leaf file/print (I have not received it; attach it). Steps: read four letters with cover off; refit cover; remove four screws and back plate; take light; refit plate; read again. Repeat in the UV-first order. Pass: identical reading, nothing loose, notches line up. CAD prediction: hole positions are frozen and the plate cannot drop a mask (integral floor); fit repeatability untested on the sheet.

## 2. M-72 (priority 2: paper only)
Paper overlay test with windows **p4/p6/p8** (`m72_paper_overlay_template_NONPRODUCTION.pdf`) AND **p4/p8/p10** (`m72_paper_overlay_template_p4_p8_p10_NONPRODUCTION.pdf`). Print at 100 % (check the 100 mm bar), cut on solid lines, punch the three head holes.
CAD comparison (signature = what the three windows show):
| | p4/p6/p8 | p4/p8/p10 |
|---|---|---|
| Correct state shows | IV/TREE, VI/DIAMOND, VIII/SUN | IV/TREE, VIII/SUN, X/KEY |
| DIAMOND visible at correct calibration | yes | no |
| 144 settings, all signatures distinct | yes | yes |
| Wrong states showing 3 of the 6 correct glyphs | 22 (11 outer-only, 11 inner-only) | 22 (same) |
| Heads (CAD angles 25/150/270, r 45) vs windows | radially clear | radially clear |
**Prediction only; both arrangements are equally discriminating.** Story note for Keeper: p4/p8/p10 puts SUN (final-synchronisation symbol) and KEY (Music House answer) in the windows; p4/p6/p8 puts DIAMOND there. That is a content decision, not an engineering one. Physical items: does the paper sit on the heads, are all glyphs readable, can a player tell which window is which. No rigid plate approved; one proof print may follow a good paper test. Files: `concepts/m72_attachment/m72_signature_table_p4_p8_p10.csv`.

## 3. Music House keyed lid (priority 3, Friday 20 Nov, only if it does not displace 1 or 2)
**Nonproduction.** Needs the cover removed first. The **lid** stays captive to the plate (three hooks); the key is a separate loose tool. Five replacement backplates are NOT authorised.
Print: `kl_coupon_NONPRODUCTION.stl` (plate centre r 34 with floor, holes and three hooks, 68 mm, about 15 min), `kl_lid_lug06_...` and `kl_lid_lug08_...` (lug clearance 0.5 and 0.3 mm, about 6 min each), `kl_key_long_...` (tongue 16 mm; the socket is 15 mm below the deck top; about 8 min). Total about 35 min, one bed.
Tests (all PHYS; CAD column is geometry only):
| Test | Method | CAD | PHYS |
|---|---|---|---|
| Hook strength | push lid up from below through a floor hole until it gives, or hang a known weight | locked lift 1 mm stops at hooks (chk_kl_locked_lift NON-EMPTY = stopped) | |
| Reliable opening | key in, turn about 32 degrees anticlockwise to the gap, lift, 10 times | free to lift at 36 degrees (chk_kl_unlocked_lift EMPTY) | |
| Inadvertent release | shake, invert, tap, press on lid by hand | cannot rotate without the key (socket recessed) | |
| Repeated use | 20 lock/unlock cycles; look for cracked hooks | not predicted | |
| Fit on existing plate | lid and key on a finished plate in the instrument | apertures untouched; arbor clear of cover | |
**Abandon rule:** if the first prototype needs significant refinement (hooks break, lid binds, cannot open reliably in 3 tries), recommend **dropping it for 29 Nov.** Existing plates cannot be retrofitted; a keyed lid would need new plates, which are not authorised.
CAD checks run now: chk_kl_added_in_holes, hooks_base, hooks_cover, key_arbor, arbor_under_cover, free_turn, unlocked_lift all EMPTY; locked_lift NON-EMPTY as intended.

## 4. Registration and spares
- Test the actual compositor proof from above and at 50 to 70 degrees before accepting side-view notch alignment. CAD: the black outer ring hides the fixed notch from directly above (groove visible height = 14.2 x cos(elevation): 0 mm at 90, 4.9 mm at 70, 7.1 at 60, 9.1 at 50). PHYS: can a player align notches from above at all? If not, a printed top-view mark is a Keeper/Scribe decision.
- Four matching production instruments are the priority. The white-ring prototype is an emergency spare only if it passes the same functional tests (1A to 1C and registration).
- Spare small parts: keep rejected-but-functional strips, caps, rings, screws and the spare tile set where capacity permits.

## 5. Print order (no daytime interaction)
1. Tonight overnight: stiffer strips t0.9 and t1.0 (about 10 min bed; fits any slot), then outer rings from the queue.
2. Before work Fri: keyed-lid coupon plus lids plus key (35 min), only if tonight's strips are done.
3. Evening: production plates/bases per `PRINT_QUEUE_2026-11-18.md` (gate decks wait on test 1A).
Need from owner: 1A result; which strip you printed (0.7 or 0.8); journal leaf; stock inventory; four tile sets; screw-head measurements; Phillips size.
