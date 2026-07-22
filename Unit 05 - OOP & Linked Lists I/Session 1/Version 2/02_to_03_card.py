'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 2
  Problem 2: Print Card / Verify Update
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
    def print_card(self):
        print(f'{self.rank} of {self.suit}')


# Problem 2: create `card` (suit 'Clubs', rank 'Ace') and call card.print_card().
# Problem 3: update card's suit to 'Hearts', then print again.
card = None  # your code


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import check_setup

check_setup()   # ▶ Run this file to validate your work
