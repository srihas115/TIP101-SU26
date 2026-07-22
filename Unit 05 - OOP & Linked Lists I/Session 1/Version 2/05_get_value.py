'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 2
  Problem 5: Get Value
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
        pass

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-digit numeric rank")
print("  expected:", 2, "| got:", Card("Hearts", "2").get_value())

print("Test 2 - rank '10'")
print("  expected:", 10, "| got:", Card("Clubs", "10").get_value())

print("Test 3 - rank 'Queen'")
print("  expected:", 12, "| got:", Card("Diamonds", "Queen").get_value())

print("Test 4 - rank 'King'")
print("  expected:", 13, "| got:", Card("Clubs", "King").get_value())

print("Test 5 - invalid rank")
print("  expected:", None, "| got:", Card("Hearts", "Joker").get_value())


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

grade(Card)   # ▶ Run this file to validate your work
