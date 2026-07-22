class Player():
    def  __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def add_item(self, item_name):
        pass

player_one = Player("Yoshi", "Dolphin Dasher")
# items = []

player_one.add_item("red shell")
# items = ["red shell"]

player_one.add_item("super star")
# items = ["red shell", "super star"]

player_one.add_item("super smash")
# items = ["red shell", "super star"]


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

grade(Player)   # ▶ Run this file to validate your work
