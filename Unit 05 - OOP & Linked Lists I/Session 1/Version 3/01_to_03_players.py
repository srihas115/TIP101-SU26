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
