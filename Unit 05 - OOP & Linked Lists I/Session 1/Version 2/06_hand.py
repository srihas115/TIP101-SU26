'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 2
  Problem 6: Hand Class
  Write your solution in the space provided below, then click ▶ Run to validate it.
  (Full instructions and examples are in the problem set.)

  ⚠️  Keep every class, method, and function name exactly as the problem gives it,
      and use the exact variable names it asks for — the problem set solution validator looks those up
      by name (they're case-sensitive). If it can't find one, the results will tell
      you which name is missing.
==============================================================================
'''


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        pass

    def remove_card(self, card):
        pass

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]
print([c.rank for c in player1_hand.cards])

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - a new hand starts empty")
fresh_hand = Hand()
print("  expected:", [], "| got:", [c.rank for c in fresh_hand.cards])

print("Test 2 - adding a single card")
h2 = Hand()
c1 = Card("Hearts", "5")
h2.add_card(c1)
print("  expected:", ["5"], "| got:", [c.rank for c in h2.cards])

print("Test 3 - adding a second card preserves order")
c2 = Card("Clubs", "9")
h2.add_card(c2)
print("  expected:", ["5", "9"], "| got:", [c.rank for c in h2.cards])

print("Test 4 - removing a card leaves the rest")
h2.remove_card(c1)
print("  expected:", ["9"], "| got:", [c.rank for c in h2.cards])

print("Test 5 - adding the same card object twice allows duplicates")
h3 = Hand()
dup_card = Card("Spades", "Ace")
h3.add_card(dup_card)
h3.add_card(dup_card)
print("  expected:", ["Ace", "Ace"], "| got:", [c.rank for c in h3.cards])


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade

grade(Hand)   # ▶ Run this file to validate your work
