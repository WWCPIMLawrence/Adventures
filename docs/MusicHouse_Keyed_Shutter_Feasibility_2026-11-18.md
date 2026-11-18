# Music House keyed aperture shutter: feasibility study (Cog to Keeper, 18 Nov 2026)

**Status: assessment and a non-production concept only.** No approved CAD, aperture coordinate, ring, fragment, cover, base or backplate geometry was changed; no print job was started. All new files are under `concepts/music_house_shutter/`. Nothing here has been printed or physically tested.

## Recommendation: SIMPLIFY (conditional prototype, no change to the production plates yet)
1. **Do not print any more of the current backplates than the two you already have for the journal test**, until a one-bed prototype of the keyed lid (below) passes on Fri 20. The current plate is validated and is the critical part; a retained cover **cannot be added to the existing plates** (they would need reprinting).
2. **A captive rotating or sliding shutter is not practical. It is rejected** on geometry (numbers below). What *is* feasible is a **keyed bayonet lid** that locks onto a replacement plate and is turned and lifted with a clock-winding key.
3. **If the Fri 20 prototype fails, or time runs short, keep the working plate and do not add the mechanism.** The discovery can then be gated by the paper and the clue instead.

## 1. The decisive finding: a shutter disc cannot close the four holes
Because the shutter must show the same four holes at "open", a disc that turns about the plate centre needs a rotation angle at which none of its holes overlaps any floor hole. **There is none** (script `shutter_angles.py`):
- At the obvious 180 degrees the holes still overlap (one pair is only 2.5 mm apart).
- The best angle (44 degrees) still leaves **13 % of the open area uncovered** (45 mm2 of 346 mm2), enough to read part of a letter.
- A **sliding** shutter needs at least 10.5 mm of travel and a disc **52 mm across to still cover the farthest hole** (the well is 50 mm), so its pocket would have to reach about r 36 mm under the base, and it needs a linear drive.
- A **swing** shutter would need a pivot about 85 mm from the centre.
- The only window available inside the plate's own thickness is 0.8 mm tall (the plate is 2.0 mm, the floor 1.2). So concept A is rejected.

## 2. What the CAD allows
- **Where anything can live:** inside the well, above the plate floor. The well is r 25 mm and about 16 mm deep, and **nothing of the base is inside it**; the cover's skirt is 10 mm or more above. The back face must stay flat and flush on the paper, and the floor must stay untouched.
- **Existing plates cannot be retrofitted:** a retained part needs hooks standing up from the floor, which are printed with the plate. Loose, pressed-in or glued parts would not stay attached when the plate comes off.

## 3. Concepts, ranked
| Rank | Concept | Verdict |
|---|---|---|
| **1** | **Keyed bayonet lid** (B/C hybrid): a solid lid sits on the floor over all four holes, held by three bayonet lugs under three hooks on the replacement plate; a clock-winding key (square tongue) turns it about 32 degrees, then lifts it out | **Feasible by CAD; conditional proceed** (details below) |
| 2 | Paper or wax seal over the floor, with the key as a blade or seal-breaker | Zero redesign and works with the existing plates, but it only evidences tampering, and a seal must be stuck down to stay when the plate is flipped |
| 3 | Plug insert (four pegs filling the holes) | Needs the same replacement plate, but depends on friction in the holes (the old loose-mask problem); worse than the lid |
| 4 | **Captive rotating or sliding shutter (A)** | **Rejected: cannot close the holes (section 1)** |

## 4. The keyed lid (concept 1): exactly how players use it
- **At Music House (all four routes):** players remove the centre cover (press and turn, as now). At the bottom of the well they see a plain black disc with a small square socket; the four apertures are not visible. The packet's key is a **clock-winding key** (a T handle with a 4 mm square tongue). They put the tongue in the socket, **turn about 32 degrees**, then **lift the lid out** (it comes up with the key). The apertures are now open and the sighting hole is clear. They read RIFT as already planned.
- **The lid can be set aside or dropped back and turned the other way to relock.**
- **If the plate has been removed for the UV light (Red and Green):** the lid stays on the plate; the disc and socket look the same from the inside. It cannot be lifted without being turned.

## 5. CAD fit and clearance findings (nonproduction concept, `keyed_lid_concept.scad`)
All checks run against the real assembly; all as expected:
- The added hooks **overlap no hole** and **do not touch** the base, the deck or the cover (EMPTY).
- The lid **turns freely** at every angle around the hooks at rest height (EMPTY), is **stopped by the hooks if lifted 1.0 mm while locked** (SOLID), and **lifts straight out once turned to the gap** (EMPTY).
- The key's tongue **seats in the socket without touching its walls** (4.0 mm in 4.2); the lid hub stays clear of the cover.
- The concept **does not conflict with the M-72 sight plate**: the two have no overlap in the assembled coordinates, and they occupy different radial ranges (lid and hooks to r 24.75 mm, the sight plate from r 29 mm).
- Registration, notches, the sighting hole and the four screw positions are unchanged (the sighting hole is open once the lid is out). Part volumes: the plate with hooks is +0.1 cm3 on the approved plate; the lid is 1.7 cm3; the key is 1.5 cm3.
- Space budget: lid radius 22.4 (covers the farthest hole edge, 20.25, with 2.1 mm to spare); lug to post 0.3 mm; post to well wall 0.25 mm.

## 6. Answers to the twelve questions
| # | Question | Answer |
|---|---|---|
| 1 | Add to existing printed backplates? | **No.** Replacement plates are needed (new print with hooks). The two printed plates stay usable for journal tests |
| 2 | Stays attached when the plate is removed? | **Yes** (lugs under hooks) |
| 3 | Blocks all four apertures from both sides? | **Yes.** A solid lid covers every hole (and the sighting hole) |
| 4 | Key works without removing the cover or opening the UV bay? | **Not without removing the cover.** The socket is at the bottom of the well. The only back-face opening is the 2.5 mm sighting hole, too small for a square key. Removing the cover early shows only a plain disc and socket, not the reader |
| 5 | Interferes with cover release, push-and-turn, or optical reading? | **No** (the hooks and lid sit below z 4.6 mm; the cover's skirt is above 12 mm) |
| 6 | Alignment with the journal proof still possible? | **Yes.** The sighting hole and registration are unchanged once the lid is out |
| 7 | Stays closed in transport? | **Vertically yes; rotationally not yet.** There is no detent in the sketch, so hard shaking could turn the lid. Add small stops or a detent bump (design item) |
| 8 | Opens without breaking a thin key? | **Yes.** The tongue is 4 mm square (capacity about 200 N·mm; a hand-turned lid needs under 10) |
| 9 | Interferes with UV storage, screws, fragments, M-72? | **No.** Bay edge r 29.5, hooks r 24.75; no overlap with the M-72 plate |
| 10 | Risks of jamming, premature opening, lost parts, wrong reassembly? | See section 7 |
| 11 | Effort for four instruments? | Section 8 |
| 12 | Would a simple cover without a true lock deliver most of the benefit with less risk? | **Largely yes.** The risk is in the replacement plate (hooks), not the key. A plain finger-lift cover on the same hooks has the same plate risk. The zero-risk alternative is **no hardware change** and gating by paper (see the end) |

## 7. Failure modes and mitigations
- **Hooks are thin (0.55 mm post, 0.6 mm arm) and the overhang is 1.4 mm** (printed in the air): breakage or droop. Mitigate with a 45-degree gusset under each arm, or a shorter overhang with a wider arc; **test print first**.
- **Tight radial clearances (0.25 to 0.3 mm)** against print tolerance of about 0.15 mm: jamming. Tune on the coupon; a firm bevel on the lugs helps.
- **No rotational stop or detent** in the sketch: add stop tabs and a detent before any production use.
- **Finger bypass:** the socket is recessed (nothing to grip), but a determined player could twist the lid by friction through a floor hole. The family-play goal does not require more.
- **Lost parts:** the lid and the key are loose after use; keep them in the packet. The plate is usable without the lid.
- **Reassembly:** the lid has three identical lugs, so it can go on any of three ways; no wrong orientation.
- **The plate is the validated critical part.** Any hooks reprint carries risk to a working part: the reason for the conditional gate below.

## 8. Effort and schedule (estimates, P1S, calibrated from the owner's plate print)
| Step | When | Effort |
|---|---|---|
| Finish the design (stops, detent, gussets, option in the CAD, off by default) | Thu 19 | about 2 to 3 h of Cog time |
| **Prototype bed: plate centre coupon with hooks + 1 lid + 1 key** | **Fri 20 (home all day)** | about 30 min of printing |
| Test: turning, lifting, key, shake, bypass attempts, fit on a printed plate's well | Fri 20 | about 20 min |
| **Go/no-go** | Fri 20 evening | |
| If go: reprint 4 plates + 1 spare (hooks) | Sun 22 | 3 beds, about 4 h |
| Lids (5) and keys (5) | Sun 22 | about 30 min on one bed |
| Assembly and test with the real journal leaf | Mon 23 | about 2 min per instrument |

**Queue implication:** hold the overnight job of two more plates (planned Wed 18) and use that slot for an ungated job (outer rings) instead. You already have two plates for the journal test.

## 9. Does this meet the goals?
| Goal | Result |
|---|---|
| Premature exposure by early cover removal | **Addressed** (only a plain disc is visible) |
| Backplate used as a stencil after UV removal | **Addressed while the lid stays locked** |
| A reason to reassemble | **Not addressed** by hardware (the plate works detached once the lid is out) |
| A physical KEY with a real mechanical function | **Yes** (clock-winding key, square tongue) |
| Existing instrument preserved | **Yes** (nothing outside the plate changes) |

## 10. If this is not pursued
Keep the validated plate unchanged and gate the discovery with the paper and the clue: the proof leaf, and the key as a story object, can live in the Music House packet. That costs no engineering risk and no print time.

## Files
`concepts/music_house_shutter/`: `shutter_angles.py` (rotation, slide and swing analysis), `keyed_lid_concept.scad` (non-production model with all fit checks), `keyed_lid_NONPRODUCTION.stl`, `keyed_lid_key_NONPRODUCTION.stl`, `plate_with_hooks_NONPRODUCTION.stl`. Pictures: `images/kl_unlocked.png`, `images/kl_locked.png`.
