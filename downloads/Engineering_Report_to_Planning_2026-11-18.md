# Claude Code (Chronometer engineering): report to Planning against the unified handoff of 18 Nov 2026

Format requested by the handoff: completed, blocked, next action, decisions needed, plus discrepancies and missing source material. No broad revisions have been started.

## 1. Completed (all in the repository, branch `claude/brave-ramanujan-dc57dr`)
- Integral asym_v1 aperture is the CAD default; the separate mask is retired (baseline commit `09dfe49`, old exports in `stl/legacy/`). Frozen coordinates unchanged (`reference/aperture_geometry.json`, SHA-256 `a37d539b...f8aa`).
- Automatic hole read-back check added; all 25 interference checks pass.
- Owner-reported physical results on one two-colour plate: holes 10.5 mm, sighting hole 2.5 mm, flat, black floor bond holds, fits the existing base through repeated refits, **1:1 engineering template matches (R, I, F, T)**. Arrow coloured by hand, accepted.
- Gate (push-and-turn) mechanism works in the owner's hands; plain ring with ledge works; strip feet fixed in CAD (press fit, deeper): **not yet printed**.
- Production candidate files by batch, production plan, running print checklist, full status handoff (all in `downloads/`).

## 2. Blocked
1. **Knob test** (and the strip-feet test) needs the reprinted gate seat v2 and strips v2 (about 25 min of printing).
2. **Phillips screw head size** for the keystone pocket (keep the current socket-head pocket if not supplied by Thu 20).
3. **Journal proof and host overlay files**: the two documents are still not received here (ChatGPT Library links cannot be opened by Claude Code; they need to be attached).
4. **Printed inventory** not yet reported (rings, caps, tiles, pawls, brass parts).

## 3. Discrepancies and findings
1. **Date: resolved.** Hunt Sunday 29 Nov; packed by Sat 28 evening. My production plan assumed more weekend and weekday capacity than the owner has (see section 5); the schedule below replaces it.
2. **Fallback is not proven.** The handoff says the old three-arm latch is "not automatically a reliable fallback". Agreed: it fails the knob problem. My plan listed it as a fallback only for print-time purposes. **If the gate fails the knob test there is no tested alternative**; a decision would be needed then (see decisions).
3. **The fixed notch is not visible from directly above.** The black outer ring is not cut and sits directly over the notches (which run through the brass base, plate and deck rim up to the ring's underside). From above the ring hides the notch at every ring position; from the side or an oblique angle it is visible as a vertical groove (about 2.5 mm wide, 1.3 mm deep). The Music House step "align the fixed directional reference with REGISTER" is therefore an oblique-view alignment; the 9 mm tail of the REGISTER line beyond the rim (nominal) is visible from above, the notch is not. **This should be an explicit acceptance test with the real leaf**, not an assumption.
4. **Coverage by the handoff:** it says the plate-and-paper pairing has "no physical pass". Correct for the real journal leaf; the engineering template pass and hole measurements are recorded (item 1).
5. **Assembly instructions** (asked for in the Claude critical path) are not yet written for the current configuration (integral plate, gate or latch). Planned after the freeze.
6. **Old documents** still say 26 or 27 Nov, or describe a separate mask: the 16 Nov handoff PDFs. Treat `Chronometer_Full_Status_Handoff_2026-11-17.md` and this report as current.

## 4. Decisions needed from Planning
1. **If the gate fails the knob test:** (a) stiffen the strips and retest, (b) accept the latch with the clue "hold the large disc while loosening the knob" and a spare, or (c) another mechanism (extra work, not currently planned). My preference: (a), then (b).
2. **Morning job order (see section 5).** I recommend seat v2 and one base first; plates overnight.
3. **Acceptance tolerance for the notch alignment** on the real leaf (suggested: centred RIFT after alignment by eye within 1 mm, repeated after plate removal and refit).
4. **Spares:** one plate, one base, and one complete set of small parts (pawls, strips, ring)? Reduces risk, costs about 3 h of machine time.
5. **Who runs the independent solver test** on the integrated plate and the real leaf, and when (suggested Fri 20 or Sun 22).

## 5. Next actions: schedule against the owner's availability
Bed-runs needed (P1S, calibrated by the owner's plate print; two 125 mm parts fit per bed): about 15 beds, about 22 h of machine time. Weekday capacity: one morning job (runs while the owner is at work) plus one evening or overnight job.

| Date | Owner availability | Print and test plan |
|---|---|---|
| Tue 17 (tonight) | evening | 3 bases (printing) |
| Wed 18 | work | **AM: gate seat v2 + base no. 4.** Evening: PETG strips v2 (10 min), then **knob test**. Overnight: 2 back plates |
| Thu 19 | work | Decision gate or latch; **freeze**. AM/overnight: decks (2 per bed) |
| Fri 20 | off (craft-show prep shared) | Covers (4 per bed), index caps, remaining decks, keystones if the screw size is known |
| Sat 21 | unavailable | machine may run one long job (outer rings) |
| Sun 22 | production day | Rings, tiles, pawls, spares. **Assemble the pilot instrument** |
| Mon 23 to Wed 25 | work | AM job plus overnight job each day: assemble units 2 to 4 as parts finish; reprints; journal test with the real leaf; target: engineering done by Wed 25 where practical |
| Thu 26 | Thanksgiving | none |
| Fri 27 | off | Acceptance testing: both play orders with the real leaf, repeated plate refits, gate and knob; repairs |
| Sat 28 | final | Final inspection and packing |
| Sun 29 | hunt | Cache placement in the morning |

The weekday jobs only fit if the owner can restart the printer each evening. Parts that depend on the knob test (decks, covers, ring) cannot start before Wed evening.

## 6. Interface notes for Work
- Coordinates, reading order, hole sizes and the no-mirror convention are as in the unified handoff; the sighting hole is 2.5 mm over the cross (no letter under it).
- **Cover release wording** depends on the knob test: gate = press down about 1 mm and turn anticlockwise 28 degrees, then lift; latch = twist anticlockwise. Do not finalise until Claude Code reports.
- A locked gate cover stands about 1.2 mm proud: it is an inspection indicator (lower = weak springs).
