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
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def get_value(self):
        if self.suit not in ('Hearts', 'Spades', 'Clubs', 'Diamonds') or self.rank not in ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace'):
            return None
        if self.rank == 'Ace':
            return 1
        if self.rank == 'Jack':
            return 11
        if self.rank == 'Queen':
            return 12
        if self.rank == 'King':
            return 13
        return int(self.rank)
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)


def sum_hand(hand):
    pass  # write your solution here


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
