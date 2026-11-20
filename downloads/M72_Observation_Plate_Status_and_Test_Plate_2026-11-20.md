# M-72 Surveyor's Observation Plate: CAD status, test plate and what is missing (20 Nov 2026)
Reply to Keeper's reminder. CAD results are predictions; **no plate has been printed or tested**. Non-production until physically accepted. No change to any Chronometer part.

## What it is and where it stands
A separate rigid printed plate that lies over the Chronometer face and shows three **pairs of windows** (an outer-ring numeral window and an inner-ring symbol window at each clock position), so the player reads the numeral and symbol pairs and compares them with the M-72 evidence. It rests on the three index-cap screw heads (no attachment) and stays inside the outer ring's edge. It is distinct from the integrated Music House aperture. **It is on the production checklist now (row 21): 4 needed, 0 printed, one test plate first.**

## Updates made for the accepted configuration (vs the 18 Nov concept)
- **Pan-head cap screws** (Keeper's screw decision) instead of socket heads: heads assumed **6.0 mm diameter x 2.4 mm high (NOT measured)**; cups are 7.0 mm across and only 0.6 mm deep, so the plate underside stays at the same height whatever the real head height is.
- **Window chamfers made one-sided.** The old symmetric chamfer ran into the plate's edge and left a 0 to 0.1 mm sliver; now the symbol window keeps a straight inner wall (1.0 mm web at the plate's inner edge) and the numeral window a straight outer wall (1.1 mm web at the outer edge). The chamfered sides still cut parallax.
- Default window layout for the test plate: **p4 / p8 / p10** (Keeper had noted it hides DIAMOND at the correct calibration). **p4 / p6 / p8** is also exported. **Keeper or Scribe must still choose the final layout**; I have no engineering preference.

## CAD checks (predictions), both layouts, head heights 2.2, 2.4 and 3.0 mm
- **Clear of** the outer and inner rings (with their raised lettering), the index cap, the pan-head screw heads (they only touch the cup roofs), and the **gate-raised T1-v1 centre cover**: all EMPTY, so no interference is predicted. Sinking the plate 0.1 mm makes the heads hit the cup roofs (SOLID, as intended: the three heads hold the plate up) while it stays clear of rings and cap.
- **Not checked:** clearance to the real printed heads; flatness of a 2.0 mm PLA annulus (the plate may flex in the hand); parallax and readability on a real print.

## Test plate for physical acceptance
`m72_TEST_PLATE_pan_heads_p4810_NONPRODUCTION.stl` (and `..._p468_...` as the alternative): 124 x 124 x 2.0 mm, **17.1 cm3**, print **flat on the bed, underside down**, no supports (the cups are shallow recesses that bridge). Rough guess: about 1 h (not measured). Colour is a decision (see below). **Do not print before the Chronometer durability tests have room; print only this one plate, not the other three.**
Owner's physical test: (1) it rests on the three cap-screw heads, level, without touching the rings or index cap; (2) rings turn freely with it on; (3) the centre cover can be removed and refitted with it on or off (note which); (4) read the pairs at the correct calibration, **outer ring XII and inner ring STAR at the fixed arrow**: windows must show the expected numeral and symbol (p4/p8/p10: IV/TREE, VIII/SUN, X/KEY); (5) viewing from above and at an angle, are the glyphs readable and unobstructed; (6) does it rock or slide off when tilted; (7) after it comes off, nothing is marked or loose.

## What I need from Scribe (and Keeper)
1. **The final window layout** (p4/p8/p10 or p4/p6/p8) or another set: Scribe has not frozen anything until Cog and the owner report a physical reading.
2. **The M-72 evidence puzzle artwork:** which numeral-symbol pairs the windows must identify, any pair-to-answer mapping, and where the evidence is to be read (photographs, card, table). I have only the geometry, not the artwork.
3. **Window labels:** does the plate carry engraved or printed marks (for example A, B, C, a title or tick marks), and in what typeface? I have drawn none.
4. **Finish and colour** (for example matte black, bone or brass) and whether lettering or raised marks on the plate are wanted.
5. **Wording and size of any instruction** that goes with the plate.
6. **Any story constraint** on which symbols may be visible (for example avoiding DIAMOND at calibration).
## What I need from the owner
Measure one **pan-head cap screw**: head diameter and height (calipers). The plate design assumes 6.0 x 2.4 mm.

## Status of the other three plates
Not started. They wait for the physical acceptance of the test plate and for the Scribe items above.

## Update 20 Nov (after Scribe's interface review)
- **Decided for the test (Scribe):** p4/p8/p10, existing PLA, no labels or engraving, matte dark colour preferred; alternative layout NOT printed. Predicted ordered signature at outer XII and inner STAR: **IV/TREE, VIII/SUN, X/KEY**, read clockwise from the fixed arrow.
- **Orientation (CAD prediction, Scribe's question):** the three cups sit at the screw positions, which are **unevenly spaced (125, 120, 115 degrees)**. Turning the plate by 120 degrees misfits by about 5 degrees (3.9 mm at the screws) against a cup clearance of only 0.5 mm, so **only one orientation should seat**; the cups are on the underside, so it cannot sit upside down. To be confirmed physically.
- **One-click miscalibration (CAD prediction):** outer ring +1: V/TREE, IX/SUN, XI/KEY; outer -1: III/TREE, VII/SUN, IX/KEY; inner +1: IV/COMPASS, VIII/MOON, X/FLAME; inner -1: IV/HOURGLASS, VIII/EYE, X/MOON; both +1: V/COMPASS, IX/MOON, XI/FLAME; both -1: III/HOURGLASS, VII/EYE, IX/MOON. **None matches any of the three correct pairs completely**, and across all 144 settings the complete signature is unique. DIAMOND does not appear at the correct calibration (it appears at the one-click inner states only if a window shows it: it does not in these six).
- Owner's test sheet: `M72_TEST_PLATE_SHEET_2026-11-20.txt`. Owner still to measure one pan-head screw. Predictions only.

## Update 20 Nov (owner's measured screw head): the plate was REDESIGNED
- **Measured pan head: 4.6 mm wide x 1.9 mm tall** (the design had assumed 6.0 x 2.4). With the old cups (7.0 mm) the plate would have had about 1.2 mm of sideways slop, and its underside would have dropped to only about 0.3 mm above the rings.
- **New design (CAD):** the plate body is flat and sits **0.8 mm above the tallest ring feature**, as before. Three small **bosses hang below it** at the screw positions, each with a **5.2 mm cup, 1.4 mm deep** that holds the dome. Predicted sideways slop is about 0.45 mm each side; the cup roof touches only the dome's crown; the boss bottoms stay 0.5 mm above the index cap's top face.
- **CAD checks, all as required (predictions only):** clear of the rings, index cap, screw heads (they only touch the cup roofs) and the gate-raised T1-v1 cover for head heights **1.7, 1.9 and 2.1 mm**; sinking the plate 0.1 mm makes the heads hit the cup roofs (the heads hold it up) while it stays clear of rings and cap.
- **New file:** `m72_TEST_PLATE_p4_p8_p10_measured_heads_NONPRODUCTION.stl` (124 x 124 x 3.3 mm, 17.3 cm3). It replaces the two earlier test-plate files, which are withdrawn (do not print them). **Print TOP FACE DOWN** (the file is already oriented that way: smooth face on the bed, bosses and cups facing up, no supports). Unmarked, existing PLA, matte dark colour preferred, one plate only.
- Orientation: cups are 5.2 mm across at screw positions spaced unevenly (125, 120, 115 deg), so turning the plate by 120 deg misfits by about 3.9 mm: only one orientation should seat. To confirm physically.

## PHYSICAL RESULT, one test plate (owner, 20 Nov) 
Owner-reported, hand test; step 7 (one click wrong) not yet reported.
- **Seating (1):** sits nicely once properly installed. **Finding:** it is hard to tell which way round to place it; it can be misaligned without the owner realising.
- **Rings (2):** only the outer ring is reachable with the plate on and it spins with no problems; the inner ring is covered by the plate and cannot be turned (set it before fitting the plate). The plate can slip and misalign when the outer ring is twisted by hand.
- **Centre cover (3):** removes and refits with no issues.
- **Orientation (4):** connects only in one position with all three screws, but it is easy to be slightly misaligned without noticing.
- **Slipping (5):** surprisingly stable when tilted; only twisting at the top level disturbs it. The window over the fixed arrow shows the correct alignment and makes aligning easy.
- **Reading (6): the three pairs read IV/TREE, VIII/SUN, X/KEY, in that order (as predicted), visible from all angles, nothing cut off** (owner: "I see exactly what you described and in that order").
- **After removal (8):** no damage.
### Owner's suggestions for a next plate (not yet authorised)
Matching orientation notches on the plate (like the rest of the device); **magnets in the screw cups** (the owner has magnets; the cap screws are steel); a small centre hole or sight holes to show the screw heads; thematic design features, possibly with a Scribe clue. **Cog's view:** magnets in the cup roofs (self-centring, snap, resist twist), a 12 o'clock orientation mark, and small sight holes over the heads address the finding; the inner ring should be set before the plate is placed (a finger window would expose other symbols). Needs Keeper's and Scribe's approval; magnet size needed.

**Colour note (owner, 20 Nov):** the test plate was printed in **brass**, not the matte dark colour Scribe preferred. The owner had imagined it as a piece of the overall device that had been removed, so brass was intentional-by-design-thinking; the glyphs still read clearly against the black rings in the windows (photo). Final colour is a Keeper/Scribe decision; contrast against the brass instrument was the reason for Scribe's dark preference.
