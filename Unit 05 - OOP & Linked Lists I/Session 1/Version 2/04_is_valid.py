'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 2
  Problem 4: Valid Card
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

    def is_valid(self):
        pass

my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - valid suit and rank (Hearts, 7)")
print("  expected:", True, "| got:", Card("Hearts", "7").is_valid())

print("Test 2 - invalid rank (Joker)")
print("  expected:", False, "| got:", Card("Spades", "Joker").is_valid())

print("Test 3 - invalid suit")
print("  expected:", False, "| got:", Card("Stars", "King").is_valid())

print("Test 4 - valid face card rank (Ace)")
print("  expected:", True, "| got:", Card("Diamonds", "Ace").is_valid())

print("Test 5 - valid face card rank (King)")
print("  expected:", True, "| got:", Card("Clubs", "King").is_valid())

print("Test 6 - both suit and rank invalid")
print("  expected:", False, "| got:", Card("Stars", "Joker").is_valid())

print("Test 7 - rank as int instead of string (invalid, spec expects string ranks)")
print("  expected:", False, "| got:", Card("Hearts", 7).is_valid())


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
