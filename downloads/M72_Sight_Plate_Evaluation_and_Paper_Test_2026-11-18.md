# M-72 sight plate: evaluation of Keeper's eight questions, and the paper proof-of-concept test sheet

Cog to Keeper, 18 Nov 2026 (evening). **Status: nonproduction.** No production CAD changed; nothing was printed. Approved: one paper-overlay proof of concept only. Not approved: rigid plates, production CAD changes, four team copies. The outer XII / inner STAR calibration and windows A, B, C at p4 / p6 / p8 are preserved.

## Read this first
**I cannot send actual physical test results.** I have no printer, paper or instrument. What I did: checked every question against the real CAD and measured geometry, **found and fixed a real defect in my own concept**, and wrote a test sheet (section 3) whose numbers the owner can fill in at the office printer in about 20 minutes. Answers marked **CAD** are computed; answers marked **TEST** need a physical result.

## A defect found and fixed (important)
The 18 Nov concept's windows were 12 mm wide. Measured from the CAD, the widest numeral (**VIII**) is **12.6 mm wide**, and numerals are 8.2 mm tall with their rails (the window was 9.0 mm, 0.1 mm of margin on the outer edge). VIII would have been clipped even at perfect alignment (95 % visible). Symbols are at most 7.1 x 7.0 mm.
**Corrected windows (sized from the glyphs plus a registration budget):** numeral window 16.0 x 10.6 mm (r 50.3 to 60.9); symbol window 10.0 x 9.3 mm (r 29.6 to 38.9); a small window keeps the fixed arrow visible; plate inner edge now r 28.6 mm; rigid windows get a 1 mm 45-degree top chamfer. All fit checks were re-run and pass. The paper template was regenerated (same filename).

## The eight questions
| # | Question | Answer |
|---|---|---|
| 1 | Does the paper overlay seat repeatably on the real instrument? | **CAD: yes by geometry.** Three 6.4 mm holes over the 5.5 mm heads seat in exactly one orientation (within 0.5 deg, about 0.45 mm of play); turned 120 or 240 deg the heads miss by 3.9 mm; a mirrored copy cannot seat. **TEST:** T2 and T3 |
| 2 | Are all three windows readable, including one click away? | **CAD: yes.** The windows sit exactly on the rings' 30-degree glyph grid (window angle = 90 - 30p = glyph angle at every detent), so a glyph is centred at any of the 12 clicks. Picture: `images/m72_states_top_view.png` (correct state and two one-click states, whole glyphs in every window). **TEST:** T4 |
| 3 | Can players turn the rings with the overlay on, or calibrate first? | **Paper:** it lies on the raised markings (ribs at 6.4 mm), so turning a ring under it will drag; **calibrate first, then apply.** **Rigid plate:** it hovers 0.8 mm above the tallest ring feature (checked), so rings turn freely, and the arrow window lets players set them with the plate on. **TEST:** T5 |
| 4 | Fitted and removed without disturbing the cover or other mechanisms? | **CAD: yes.** The plate's inner edge (r 28.6) is 0.8 mm clear of the cover (r 27.8); no overlap with the cover locked, or lifted 1.2 mm by the gate; it lifts straight off and touches nothing else. **TEST:** T6 |
| 5 | Are the real screw-head dimensions and heights as modelled? | **Modelled:** 5.5 mm across, 3.0 mm tall, on the cap top (cap thickness 2.4), at r 45 mm, 25 / 150 / 270 deg. This equals the maximum of an ISO 4762 M3 socket head (5.32 to 5.50 across, 2.86 to 3.00 tall), so a real head is the same or slightly smaller. **TEST:** T7 (measure three heads; a button head, a washer or a low-profile head changes the answer) |
| 6 | Would the rigid version's parallax interfere with reading? | **CAD: modest.** Worst-case visible fraction of the glyph (over every viewing direction and every registration-error corner): square edges 100 / 93 / 85 / 74 % at 0 / 15 / 25 / 35 deg; **with the 1 mm chamfer 100 / 95 / 90 / 83 %.** Paper overlay: 100 / 100 / 100 / 98 %. Ordinary viewing down the well is about 0 to 25 deg, so the chamfered plate reads; the edge rails of the widest numerals are what clip first |
| 7 | Compatible with the keyed Music House shutter? | **CAD: yes.** The lid and hooks stay at r 24.75 mm or less and below 4.6 mm; the plate is at r 28.6 or more; the combined geometry has no overlap (checked). The plate works with the cover on; the keyed lid needs the cover off, so they do not interfere. The shutter is itself only a concept |
| 8 | Does the three-window signature distinguish the calibrated state fairly? | See next section |

## Question 8: the signature
- Script `signature_table.py`, full data in `m72_signature_table_all144.csv` (every ring setting and what A, B, C show) for Scribe.
- **The calibrated state's signature is A = IV / TREE, B = VI / DIAMOND, C = VIII / SUN.** All 144 settings give 144 different six-glyph signatures; **no other setting reproduces it.**
- **It depends on both rings.** Single-ring errors (one ring right, the other wrong) each show **3 of the 6 correct glyphs** (the numerals, or the symbols), so a near-miss is visible and obviously not a match; there are 22 such near-miss states, all of the "one ring right" kind. A wrong state never shows more than 3 of 6.
- **Fairness points for Scribe:**
  - Any one window already identifies both rings, so the three windows are redundant: use them for verification, or let the record quote all three so players can check themselves.
  - **At the calibrated state window B shows DIAMOND on the ring itself.** The plate does not print DIAMOND 11:11, but a player will see DIAMOND in B. If that is not wanted, choose windows where the correct state shows non-answer glyphs (for example p4, p8, p10).
  - Make each competing record's *decoy* a real single-ring error (the table lists the exact signatures), and avoid decoys that other evidence already rules out (for example a STAR 9:03 or HOURGLASS 10:26 line that the team has collected).
  - The test does not depend on XII representing zero: the numerals are used as printed.

## Rigid plate: is it worth printing? (recommendation, not approval)
- **CAD says yes, conditionally.** It seats positively on three fixed points, lets the rings turn with it on (and keeps the arrow visible), does not wear or tear, and reads well with the chamfer.
- **Cost:** about 17 cm3 and about 40 min per plate on the P1S (two per bed); 4 plates plus a spare is 3 beds, about 3.5 h. It is not in the print queue, and would use a weekday slot (suggested Mon 23 to Tue 24).
- **Print only if the paper test shows:** the overlay seats at least 9 of 10 times (T2); the glyphs read correctly at 25 degrees or less (T4); and either the paper drags the rings or tears (T5, T9), or Keeper wants a durable team copy. If the paper works fine for the hunt's number of uses, **paper may be enough** and costs no machine time.
- **If approved:** print one rigid plate first (about 40 min) for a fit test before four.

## 3. Paper proof test sheet (about 20 minutes, at the office printer)
**Materials:** the template `m72_paper_overlay_template_NONPRODUCTION.pdf` printed at 100 % on heavy cardstock (110 lb or about 200 gsm if available; plain paper is fine for a first look), a craft knife, a ruler, a 6.4 mm hole punch or the knife for the three holes, calipers.
1. **T1 Print:** check the scale bar measures 100 mm. Cut the outer and inner circles, all six windows and the small arrow window; make the three round holes.
2. **T2 Seating (Q1):** set the rings to the calibrated state (outer XII and inner STAR at the arrow). Place the overlay and remove it 10 times. Record, per cycle: dropped over the three heads on the first try? (Y/N); are all six glyphs fully visible, with none cut off? (Y/N). **Pass: 9 or more of 10 first-try seats; glyphs fully visible every time.**
3. **T3 Orientation:** try the overlay turned 120 deg, 240 deg and flipped over. **Pass: none seats** (the holes cannot all reach the heads).
4. **T4 Readability (Q2):** with the overlay on, read all three windows aloud (calibrated, then each of the four single-click states: inner one click either way, outer one click either way). View straight down, then about 25 and 35 degrees from each side. Record any glyph you cannot read and from which angle. **Pass: every glyph identified correctly at 25 degrees or less.**
5. **T5 Rings (Q3):** with the overlay on, turn each ring one full revolution. Record: does the overlay slide or lift? does it drag or snag on a rib? does a ring feel rougher? **Note the result; "calibrate first, then apply" is the expected rule for paper.**
6. **T6 Cover (Q4):** with the cover on and locked, then with it off, put on and remove the overlay 10 times. **Pass: the cover never moves or rubs; no other part is disturbed.**
7. **T7 Screw heads (Q5):** with calipers, measure each of the three index-cap screw heads: diameter and height above the cap top. Measure the centre-to-centre distances between the three heads (expected about 79.8, 77.9 and 75.9 mm). **Pass: heads 5.3 to 5.5 mm across and 2.9 to 3.0 mm tall; distances within 0.5 mm.** Note the screw type if it differs.
8. **T8 Signatures:** at each of the four single-click states, read A, B, C and compare with `m72_signature_table_all144.csv`. **Pass: they match.**
9. **T9 Wear:** after the 10 cycles, do the holes tear or the card curl?

| Test | Result | Notes |
|---|---|---|
| T2 first-try seats (of 10) | | |
| T2 glyphs fully visible each time | | |
| T3 wrong orientations seated? | | |
| T4 unreadable glyphs (which, from what angle) | | |
| T5 overlay moved or dragged? | | |
| T6 cover disturbed? | | |
| T7 head diameter / height / spacings | | |
| T8 signatures match | | |
| T9 tearing or curl | | |

## Files
`concepts/m72_attachment/`: `m72_sight_plate_concept.scad`, `m72_sight_plate_concept_NONPRODUCTION.stl`, `parallax_check.py`, `signature_table.py`, `m72_signature_table_all144.csv`, `make_paper_template.py`, `m72_paper_overlay_template_NONPRODUCTION.pdf` (regenerated). Pictures: `images/m72_states_top_view.png`, `images/m72_sight_plate_concept.png`.
