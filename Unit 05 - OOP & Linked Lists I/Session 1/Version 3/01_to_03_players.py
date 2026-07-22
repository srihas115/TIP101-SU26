'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 3
  Problem 1: Player Class / Get Player / Update Kart
  Write your solution in the space provided below, then click ▶ Run to validate it.
  (Full instructions and examples are in the problem set.)

  ⚠️  Keep every class, method, and function name exactly as the problem gives it,
      and use the exact variable names it asks for — the problem set solution validator looks those up
      by name (they're case-sensitive). If it can't find one, the results will tell
      you which name is missing.
==============================================================================
'''


class Player():
    def  __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

# --- Merged from Problem 2: Get Player.py ---
def get_player(self):
    return f"{self.character} driving the {self.kart}"

# --- Merged from Problem 3: Update Kart.py ---
print(player_one.get_player())

# < your code to update kart>

print(player_one.get_player())


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
