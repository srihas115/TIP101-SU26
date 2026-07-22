'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 2
  Problem 7: Sum of Cards
  Write your solution in the space provided below, then click ▶ Run to validate it.
  (Full instructions and examples are in the problem set.)

  ⚠️  Keep every class, method, and function name exactly as the problem gives it,
      and use the exact variable names it asks for — the problem set solution validator looks those up
      by name (they're case-sensitive). If it can't find one, the results will tell
      you which name is missing.
==============================================================================
'''


class Card():
    def  __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    #... methods from previous problems

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        pass

    def remove_card(self, card):
        pass


def sum_hand(hand):
    pass

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: expected values assume a correct get_value() (from Problem 5) and correct
# add_card()/remove_card() (from Problem 6) - fill those in for these to pass too.

print("Test 1 - empty hand")
empty_hand = Hand()
print("  expected:", 0, "| got:", sum_hand(empty_hand))

print("Test 2 - single numeric card")
h1 = Hand()
h1.add_card(Card("Hearts", "5"))
print("  expected:", 5, "| got:", sum_hand(h1))

print("Test 3 - two face cards")
h2 = Hand()
h2.add_card(Card("Hearts", "King"))
h2.add_card(Card("Clubs", "Ace"))
print("  expected:", 14, "| got:", sum_hand(h2))

print("Test 4 - hand containing an invalid card")
h3 = Hand()
h3.add_card(Card("Hearts", "5"))
h3.add_card(Card("Spades", "Joker"))
print("  expected:", None, "| got:", sum_hand(h3))


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

grade(sum_hand)   # ▶ Run this file to validate your work
