#!/usr/bin/env python3
"""Builds docs/Chronometer_gate_test_handoff.pdf - push-and-turn gate and ring ledge: test design, for the owner and ChatGPT."""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, KeepTogether

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "Chronometer_gate_test_handoff.pdf")
ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontSize=17, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontSize=12.5, spaceBefore=10, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle("B", parent=ss["BodyText"], fontSize=9.5, leading=13)
CAP = ParagraphStyle("CAP", parent=B, fontSize=8.5, textColor=colors.HexColor("#444444"), alignment=1)
CELL = ParagraphStyle("CELL", parent=B, fontSize=8.5, leading=10.5)
P = lambda t, st=B: Paragraph(t, st)
bullets = lambda items: [P("&bull;&nbsp; " + t) for t in items]


def table(rows, widths):
    t = Table([[P(c, CELL) for c in r] for r in rows], colWidths=[w * mm for w in widths], repeatRows=1)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#999999")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                           ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e2d0"))]))
    return t


def img(name, w_mm):
    from PIL import Image as PI
    path = os.path.join(ROOT, "images", name)
    w, h = PI.open(path).size
    return Image(path, width=w_mm * mm, height=w_mm * mm * h / w)


s = [P("The Chronometer &mdash; push-and-turn gate and ring ledge: test design", H1),
     P("<b>Status: prototype design with computer checks only. Nothing has been printed or physically tested, and the "
       "production geometry is unchanged</b> (every default part re-exports identical in volume and size; the 27 existing "
       "interference checks still pass). Everything here is an optional variant, off by default in the CAD.", B),
     Spacer(1, 3),
     P("<b>To the reviewer (ChatGPT).</b> Sections 2, 5 and 6 contain the decisions and the risks. "
       "The bayonet direction (anticlockwise to release) and the bayonet lugs are unchanged, as you asked.", B),

     P("1. Why the cover comes off when the knob is loosened (and why the ring falls out)", H2)]
s += bullets([
    "The knob's screw threads into a nut held by the cover, and the knob presses the tiles that sit on the cover. The cover is "
    "therefore the <i>only</i> part that reacts the torque a player puts into the knob, and that torque goes into the cover "
    "in the same direction as the knob turns. Loosening is anticlockwise, which is the cover's unlocking direction.",
    "The three-arm latch holds roughly 75 N&middot;mm (3 nubs x ~1 N x 25 mm; an estimate). A hand-tight M3 knob is plausibly "
    "100&ndash;300 N&middot;mm (also an estimate, not measured). So the latch loses, and its PETG arms creep, which matches "
    "the weakening after a few openings. Making the arms stiffer cannot fix this.",
    "<b>Reversing the lock direction would not have fixed it</b>: loosening would then push the cover into its stop, but "
    "tightening would push it toward release. It only swaps the problem. We agreed to keep the direction.",
    "The ring falls out because the 45&deg; retaining bump is a ramp: the ring's weight pushes it <i>inward</i>, and a split "
    "PETG ring needs almost no force to contract (about 0.05 N by beam theory). A positive catch needs a flat face."])

s += [P("2. The push-and-turn gate", H2),
      P("Each of the three lugs gets a pocket at the locked end of its track, 0.9 mm deeper than the rest of the track and "
        "ending in a vertical wall. Printed bow springs in the hub lift the cover about 1.2 mm, so its lugs rise into the "
        "pockets. While the cover is up, the wall stops the unlocking turn, so the knob cannot reach it. To unlock, the player "
        "presses the cover down about 1 mm (about 9 N), which takes the lugs under the wall, and turns it anticlockwise. "
        "Locking is the same in reverse: press, turn clockwise to the stop, let go, and the cover pops up into the pockets "
        "(the click). Cover lugs, hard stop and 28&deg; travel are unchanged.", B),
      Spacer(1, 3), img("gate_track.png", 175),
      P("Figure 1. The track unrolled at the lugs' radius (nominal dimensions).", CAP), Spacer(1, 3),
      img("gate_view.png", 120),
      P("Figure 2. Seat (brown), six bow springs (red) in pockets in the hub, and the cover (gold) lifted above it.", CAP)]

s += [P("3. The springs", H2),
      P("The hub is only a 3 mm wide ring, and there is no room for a coil or a wave washer. The springs are thin PETG strips "
        "arched in the vertical plane, <b>printed on their side</b> so there are no overhangs and the layers run along the strip. "
        "Six of them, 14 mm long, sit in straight pockets in the gaps between the cover's tracks. This is only possible because "
        "the three-arm latch is removed in this variant: its grooves occupy the same part of the hub.", B),
      Spacer(1, 3),
      table([["Strip", "Stiffness, 6 strips", "Peak strain", "Press to unlock", "Note"],
             ["soft, 0.7 mm PETG", "8 N/mm", "1.7 %", "8&ndash;10 N", "may slice as thin-wall; check preview"],
             ["firm, 0.8 mm PETG", "12 N/mm", "2.0 %", "12&ndash;14 N", "two full perimeters"]],
            [34, 32, 22, 30, 52]),
      P("Beam theory, frictionless ends (a lower bound on stiffness). Friction, the real printed modulus and creep are "
        "unknown: that is what the test is for. The springs are consumables, and there is a built-in indicator: a healthy "
        "locked cover stands about 1.2 mm proud, and if it sits low, the strips need replacing.", CAP)]

s += [P("4. Ring ledge", H2),
      P("The three bumps are replaced by a continuous inward ledge below the ring: a flat catch face 0.7 mm deep (normal along "
        "the axis, so a load on the ring cannot cam it inward) with a 30&deg; lead-in on the side the ring is pressed in from. "
        "It prints as a short 0.7 mm overhang, with no supports. The ring closes up like a circlip to pass it and opens again "
        "above it; removal for UV-disc service is the same motion in reverse (pinch the two tabs, pull). The ledge sits below the "
        "ring, so it cannot restrict the three-arm ring's spring arms either. Two test covers are provided: the gate cover (no "
        "slots, plain ring) and a cover that keeps today's three slots and three-arm ring with only the ledge changed, so the "
        "ledge can be tested on its own.", B)]

s += [P("5. Can the gate simplify the three-arm latch?", H2)]
s += bullets([
    "<b>Yes, and the test variant removes it:</b> no arms, no nubs, no cover slots, no deck grooves. The ring becomes a plain "
    "split ring. This removes the part that creeps and wears, and frees the hub space the springs need.",
    "What is lost: the arms' tactile click and their light transport hold. The pocket 'pop-up' replaces the click, and the "
    "spring keeps the cover from rattling.",
    "The cover has about 1&deg; of free turn inside its pockets (the slack that lets the lugs rise despite print tolerance). "
    "I can tighten it after the test.",
    "<b>Recommendation:</b> test the gate-only variant. Keep the current three-arm cover, ring and deck as the fallback; "
    "nothing in the production files has been touched."])

s += [P("6. The five checks you asked for", H2),
      table([["Check", "Computer result", "Needs a physical test"],
             ["Loosening or tightening the M3&times;10 knob cannot release the cover",
              "Wall engagement confirmed by overlap: lift &ge; 0.6 mm blocks the turn, pressed down it is free (probe table below). "
              "Wall holds &gt; 1000 N&middot;mm at about 10 MPa. Tightening pushes into the hard stop.",
              "<b>Yes (T2).</b> Residual risk: pressing the knob down by about 8&ndash;14 N while unscrewing would lower the cover "
              "and release it."],
             ["Doesn't interfere with the numbered fragments or knob",
              "Fragments and knob ride up with the cover (1.2 mm), clearances unchanged. Cover/knob/fragment checks pass.",
              "Feel of the assembled stack (T1)."],
             ["Accessible and comfortable",
              "Press 8&ndash;14 N over 1 mm, turn 28&deg; (turning drag about 70 N&middot;mm). Flat 55 mm top to press on.",
              "<b>Yes (T1, T4).</b> A smooth rim gives little grip; weak hands are the question."],
             ["Ring captured, spring movement free",
              "Ledge clears the seated ring and the arm ring's movement; a ring slipped 0.6 mm is caught (both checked).",
              "Hold and deliberate removal (T6)."],
             ["Stencil, flashlight bay, rings compatible",
              "Base, back plate, mask, both rings, index cap, keystone and fragments re-export <b>identical</b> with the "
              "variant on. All 12 stack checks pass in the variant.",
              "Full assembly later."]],
            [40, 78, 52]),
      Spacer(1, 3),
      P("Gate probe (cover pressed or lifted, then turned 3&deg; the unlocking way against the deck): lift 0 &rarr; free; "
        "0.4 &rarr; free; 0.6 &rarr; wall contact; 0.9 &rarr; contact; 1.2 &rarr; contact; 1.5 &rarr; hits the pocket ceiling "
        "(so the springs may not lift the cover that far). Nominal dimensions: print droop of about 0.4 mm on the 45&deg; "
        "ceilings changes both the track and the pocket, so the step should survive, but this is untested.", CAP)]

s += [P("7. What I'd print and how to judge it", H2)]
s += bullets([
    "<b>Print:</b> test seat, gate cover, plain ring (PETG), six soft and six firm strips (PETG), and optionally the "
    "ledge-only cover. Everything else is unchanged. Seven focused tests, with PASS criteria, are in the print guide "
    "(T1&ndash;T7): feel, knob loosening with 0 and 4 fragments, casual twisting by people who haven't seen it, weak-grip release, "
    "200-cycle spring life, ring retention and shake.",
    "<b>Reprints needed for production if it passes:</b> deck, cover, ring and the bows only. The base, back plate, mask, "
    "rings and index cap stay as they are.",
    "<b>If the springs fail</b> (too weak, creeping, or too stiff): the gate geometry is independent of the spring. The strip "
    "thickness and lift can change, or the springs can become a small hardware part. If the gate itself fails, the "
    "current three-arm latch is still the fallback."])

s += [P("8. Questions for the reviewer", H2)]
s += bullets([
    "Is a roughly 9&ndash;14 N press, plus a 1 mm stroke, acceptable for children and for players with weak grip?",
    "A locked cover standing 1.2 mm proud: acceptable cosmetically, or should the stroke be reduced (needs a new spring design)?",
    "Should the story clue say 'press the dial in and turn it back'? The Music House can explain it with the time-reversal theme.",
    "Should the game ever require a player to remove the cover on purpose? If not, the gate could be made stiffer.",
    "The owner will say whether the last tests used the old or the updated three-slot cover; that affects how to read the old latch results."])

SimpleDocTemplate(OUT, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
                  title="Chronometer - push-and-turn gate and ring ledge: test design").build(s)
print("ok", OUT)
