# Materials, filament and shopping list

Based on the CAD as of the first review round (running-fit bayonet with latch ring, 12 mm
base, flat UV light). Nothing here changes the CAD. Nothing has been ordered.

**How the numbers were obtained**

- **Measured (slicer):** every STL was sliced with PrusaSlicer 2.7 — 0.20 mm layers, 0.4 mm
  nozzle, 3 walls, 5 top / 4 bottom layers, 15 % gyroid, no supports, density 1.24 g/cm³.
  This is not Bambu Studio; expect your own slices to differ by roughly ±10–15 %. Matte PLA
  is denser (about 1.3 g/cm³), so matte parts will weigh a few percent more than listed.
- **Calculated:** totals, spares and allowances are arithmetic on those weights.
- **Assumed:** 25 % failed-print allowance; spare quantities; single-colour plates (no AMS
  purge). AMS colour inlays add purge waste that is not included.
- **Not verified:** product names, stock, prices and delivery. Check each yourself.

## A. Component-by-component table

Weights are per part, slicer-measured. "4×" is the quantity for four instruments.

### Printed parts

| Part | Per unit | 4× | Material | Colour | g each | Precise fit? | Material appropriate? |
|---|---|---|---|---|---|---|---|
| `base` | 1 | 4 | PLA (metallic-effect or plain) | Antique brass | 49.4 | Medium — mask seat, door dovetail | Yes. Not silk. |
| `deck` | 1 | 4 | PLA, same spool as base | Antique brass | 30.2 | **High** — ring journals, bayonet seat, latch grooves | Yes if the spool prints dimensionally like plain PLA — **prototype test**. Not silk. |
| `index_cap` | 1 | 4 | PLA | Antique brass | 7.4 | Low | Yes |
| `cover` | 1 | 4 | PLA | Antique brass | 10.2 | **High** — bayonet lugs, nut pocket, peg sockets | Yes; **prototype test** in the final filament. Not silk. |
| `door` | 1 | 4 | PLA, same spool as base (it must disappear into the back) | Antique brass | 4.2 | **High** — dovetail, side spring | Acceptable. Spring strain ~0.6 %, used rarely. **Prototype test.** |
| `outer_ring` | 1 | 4 | Matte PLA | Charcoal | 18.6 | **High** — journal, detent scallops | Yes. Matte is slightly rougher on the journal — **prototype test** for drag. |
| `keystone` | 1 | 4 | Matte PLA | Charcoal | 1.4 | Medium — screw-head press fit | Yes |
| `mask` | 1 | 4 | Matte PLA | Black or charcoal | 2.3 | Medium — spring arms | Yes. Matte is the right finish (no glare in the well). |
| `inner_ring` | 1 | 4 | Matte PLA | Aged ivory / bone | 11.0 | **High** — journal, detent scallops | Yes |
| `fragment_1…4` | 4 | 16 | Matte PLA | Aged ivory / bone | 1.3 | Medium — keying pegs, bevel | Yes |
| `pawl_outer` | 2 | 8 | **PETG** | Any (hidden) | 0.16 | **High** — springs | Yes, preferred — see below |
| `pawl_inner` | 2 | 8 | **PETG** | Any (hidden) | 0.15 | **High** — springs | Yes, preferred |
| `uv_ring` | 1 | 4 | **PETG** | Dark (seen only inside the cover) | 0.6 | **High** — latch spring | Yes, preferred |

Per instrument: 18 printed parts, **141 g**.

**PETG or PLA for the springs?** PETG for the final pawls and latch ring. PLA is stiffer but
brittle and relaxes if a ring is left between clicks; PETG tolerates several times the
strain and does not snap. PETG is also about a third less stiff, so the click will be
softer at the same thickness — start with the 1.4 mm pawls in PETG and the 1.2 mm in PLA and
compare. The mask's spring arms and the door's side spring stay PLA because those parts
must be matte black and base-coloured respectively; both are low-strain and rarely cycled.

**Metallic, silk or matte for the brass parts?**

- **Silk PLA: no.** It is the shiny "toy gold" you want to avoid, has weaker layer bonding
  and swells at the nozzle, which is wrong for the deck, cover and door.
- **Metallic-effect PLA (fine metallic pigment, satin sheen, sold as "PLA Metal" or
  "metallic"): best look.** It behaves close to plain PLA, but confirm with the deck/cover
  fit test before committing.
- **Matte PLA in a bronze / brass-brown: safe fallback.** Less metallic, but ages well with
  a dark wash and metallic wax (section F, optional).
- Avoid metal-*filled* (real brass/bronze powder) filament: abrasive and brittle.

**Not suitable anywhere:** TPU (nothing here should be soft), wood-filled (weak, fuzzy on
0.4 mm detail), glow-in-the-dark (abrasive, off-palette), transparency sheets (not used).

### Non-printed parts

| Item | Per unit | 4× | Essential? |
|---|---|---|---|
| M3 × 16 socket-head cap screw | 3 | 12 | Essential |
| M3 × 8 socket-head cap screw | 1 | 4 | Essential |
| M3 hex nut | 1 | 4 | Essential |
| Keychain UV light | 1 | 4 | Essential (owned) |
| Symbol labels (sticker paper) | 12 labels = 1 printed ring | 4 rings | Essential |
| UV insert disc (paper) | 1 | 4 | Essential |
| Self-adhesive felt strip, ~6 × 40 mm | 2 | 8 | Recommended |
| Clue sheets (paper) | as the game needs | — | Essential |

No magnets, washers, springs, inserts or glue are required by the design.

## B. Filament checklist (compare with your inventory)

Ranked by importance. "Need" already includes spares, 25 % failures and the prototype.

| # | Filament | Finish to look for | Need | Have? |
|---|---|---|---|---|
| 1 | PLA — antique brass | Metallic-effect (not silk), muted gold-brown; or matte bronze | **~700 g** (one full 1 kg spool) | ☐ |
| 2 | Matte PLA — charcoal / near-black | Matte | ~150 g | ☐ |
| 3 | Matte PLA — aged ivory / bone | Matte, warm off-white (not bright white) | ~110 g | ☐ |
| 4 | PETG — any colour, dark preferred | — | ~20 g | ☐ |
| 5 | Any PLA for fit tests | — | ~100 g | ☐ |
| 6 | *Optional:* PLA — dark bronze / copper brown | Metallic-effect or matte | ~60 g if used for index cap + keystone | ☐ |

A partial spool is fine for 2–5. For 1, use a single spool for all brass parts so the base,
door, cover and index ring match; check the spool has at least 700 g left.

## C. Hardware shopping list

Verified against the current model:

- **Cap screws:** index cap 2.4 + rib 3.0 + deck floor 2.0 = 7.4 mm of clearance hole, then
  a 10.5 mm deep pilot in the 12 mm base. M3 × 16 gives 8.6 mm of thread. **M3 × 20 no
  longer fits** — it would bottom out (it did fit the earlier, thicker base).
- **Keystone screw:** 3.8 mm of knob under the head, then 1.4 mm of cover and the 2.4 mm
  nut. M3 × 8 ends flush with the nut. M3 × 10 would also work (it passes through the hole
  in the UV disc); M3 × 6 is too short.
- **Nut:** the pocket is cut for a standard 5.5 mm across-flats, 2.4 mm thick nut.

| Item | Exact specification | Per unit | 4× | Spares | Buy total | Essential? | Likely source |
|---|---|---|---|---|---|---|---|
| Cap screw | M3 × 16 mm, socket-head cap (ISO 4762 / DIN 912), fully threaded, 5.5 mm head | 3 | 12 | 6 | 18 | Essential | Your assortment; hardware-store metric drawers; Amazon M3 socket-cap assortment |
| Keystone screw | M3 × 8 mm, socket-head cap, same standard (the round 5.5 mm head presses into the knob — button or pan heads will not hold) | 1 | 4 | 3 | 7 | Essential | Same |
| Nut | M3 plain hex, ISO 4032 / DIN 934 (5.5 mm AF, 2.4 mm thick). Not nyloc, not square, not flanged | 1 | 4 | 4 | 8 | Essential | Same |
| Draw-in screw (tool) | Any M3 × 20–30 mm, to pull the nut into its pocket | — | 1 | — | 1 | Essential tool | Your assortment |
| Hex key | 2.5 mm, for M3 socket caps | — | 1 | — | 1 | Essential tool | Likely owned |
| Sticker paper (only if printed symbols are not adopted — see `SYMBOL_TEST.md`) | Full-sheet, **matte**, Letter size, **laser-compatible** (the owner has a colour laser printer; inkjet vinyl must not be used in it); white, or cream/ivory for the aged look | 1 ring | 4 rings | — | 5–10 sheets | Essential | Office-supply or craft store; Amazon |
| UV disc paper | Uncoated paper **without optical brighteners** (natural/cream, cotton or kraft). Ordinary bright-white copy paper glows blue under UV and hides UV ink — test a scrap with your marker and light first | 1 | 4 | 8 | a few sheets | Essential | Office-supply or craft store; possibly owned |
| Felt | Self-adhesive felt, about 1 mm thick, cut to 6 × 40 mm | 2 | 8 | 4 | 1 small sheet | Recommended | Craft or hardware store (furniture-pad felt) |
| CA glue | Any thin cyanoacrylate, one drop per keystone screw head | — | — | — | 1 tube | Optional — only if a screw head spins in its knob | Likely owned |
| Label protection | Matte clear self-adhesive laminate, or matte clear spray | — | — | — | 1 | Optional but sensible — fingers rub the inner-ring labels | Office-supply or craft store |

If you would rather the three face screws looked period-correct, solid brass or black-oxide
M3 × 16 socket caps are a direct swap (optional, cosmetic).

## D. Filament consumption

Slicer-measured weights, summed.

| Colour / material | One instrument | Four instruments | Spares | ×1.25 failure allowance | Prototype round | **Total to have** |
|---|---|---|---|---|---|---|
| Antique brass PLA (base, deck, index cap, cover, door) | 101 g | 406 g | 19 g (1 cover, 2 doors) | 531 g | ~160 g | **~700 g** |
| Charcoal matte PLA (outer ring, keystone, mask) | 22 g | 89 g | 11 g (4 masks, 1 keystone) | 125 g | ~25 g | **~150 g** |
| Ivory matte PLA (inner ring, 4 fragments) | 16 g | 65 g | 5 g (1 fragment set) | 88 g | ~20 g | **~110 g** |
| PETG (4 pawls, latch ring) | 1.2 g | 5 g | 8 g (2 extra pawl sets and 1 ring per unit) | 16 g | ~4 g | **~20 g** |
| **All** | **141 g** | **565 g** | **43 g** | **760 g** | **~210 g** | **~980 g** |

Prototype round = one complete instrument, the `test_seat` (9 g) and `test_uv_bay` (11 g)
fit pieces, the mixed-stiffness pawl plate (4 g), and about 40 g of repeat prints while
tuning. It can be printed in any PLA, **except** that the deck, cover, one ring and the
springs should be repeated once in the final filaments, because fit and click depend on the
material. `test_base` (49 g) is no longer worth printing — `test_screw_ring` (23 g) replaces it for
the ring test.

Print time by the same slicer, generic machine profile (your P1S will be faster): about
15 hours per instrument, of which the base is 4½ and the deck 3½.

## E. Print assignments

One material per plate; no supports anywhere. Single-colour plates need no AMS swaps.

| Plate | Filament | Parts (one instrument) | Notes |
|---|---|---|---|
| 1 | Brass PLA | `base` | Back face down. |
| 2 | Brass PLA | `deck` | Outer wall first for accurate journals. |
| 3 | Brass PLA | `index_cap`, `cover`, `door` | Cover prints face down: the build plate sets its finish — textured PEI gives a more antique face than a smooth plate. |
| 4 | Charcoal matte PLA | `outer_ring`, `keystone`, `mask` | |
| 5 | Ivory matte PLA | `inner_ring`, `plate_fragments` | Fragments print text down, so the plate texture shows on their faces too. |
| 6 | PETG | `pawl_outer` ×2, `pawl_inner` ×2, `uv_ring` | Separate plate: PETG temperatures and plate prep differ from PLA. |

For production, plates 3–6 can each hold four instruments' worth; plates 1 and 2 hold one
base or deck each (125 mm) or four per plate if arranged 2 × 2 on the 256 mm bed.

**AMS colour inlay (optional).** Ivory numerals in the charcoal outer ring and charcoal
characters in the ivory fragments are possible by painting those faces in Bambu Studio.
Each is a two-colour PLA plate with a purge tower. The no-AMS alternative is paint-fill
(section F). Decide after the prototype; neither affects function.

## F. Purchasing recommendations

With under two weeks, anything you do not already own in category A or B should be ordered
in the same order — do not wait for the prototype to order final filament.

**A. Essential — obtain immediately (to build and test)**

1. Any missing hardware: 3 × M3 × 16 and 1 × M3 × 8 socket-head cap screws, 1 × M3 hex nut
   (for the prototype; 18 / 7 / 8 in total).
2. PETG, any colour, if you have none usable.
3. The antique-brass PLA, because the deck/cover fit must be proven in it.

**B. Essential — obtain before final production**

4. Charcoal matte PLA and ivory matte PLA, if not in your inventory.
5. Matte sticker paper for the dial labels.
6. Non-brightened paper for the UV discs (after testing what you have).
7. Felt.

**C. Optional — cosmetic**

8. Cream/ivory sticker paper instead of white.
9. Acrylic paint, ivory or bone, to fill the engraved numerals and index arrow (wipe-off
   paint-fill), if you skip the AMS inlay.
10. Dark brown or black acrylic wash, and an antique-gold metallic wax, to age the brass
    parts. Keep both off the ring journals, the bayonet and the door slides.
11. Matte clear coat or laminate over the labels.
12. Brass or black-oxide face screws.
13. A dark-bronze PLA for the index cap and keystone as a second metal tone.

**Can be omitted:** magnets, washers, heat-set inserts, threadlocker, TPU, wood-filled and
glow filament, transparency sheets.

**Where to look** (I have not checked stock, price or delivery for any of these):

- *Filament:* search by finish, not by brand colour name — "metallic PLA antique brass /
  bronze (not silk)", "matte PLA charcoal", "matte PLA ivory / bone white". Bambu Lab's own
  PLA Metal and PLA Matte ranges and Polymaker's matte PLA are the kind of product meant;
  confirm the exact colour from photos of printed parts, and confirm the delivery date
  before ordering.
- *Hardware:* a metric M3 socket-head-cap assortment covering 8 and 16 mm lengths with hex
  nuts covers everything; hardware stores usually stock these lengths individually.
- *Paper, felt, paint:* office-supply and craft stores.

## Selections that need a prototype test

1. Metallic-effect brass PLA on the **deck** and **cover**: ring journals, bayonet, latch.
2. PETG **pawls** at 1.2 and 1.4 mm against PLA at 1.2 mm: click strength and settling.
3. PETG **latch ring**: cover retention and click.
4. Matte PLA **rings** on the brass deck: drag.
5. **Door** in the brass PLA: slide, click, spring survival.
6. **UV disc paper** under your actual light and marker.
7. **Sticker stock** in the 0.4 mm label pockets: thickness and adhesion to the ring.
