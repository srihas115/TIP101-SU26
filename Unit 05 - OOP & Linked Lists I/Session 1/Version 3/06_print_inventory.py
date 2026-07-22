class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def print_inventory(self):
        pass

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - player with no items")
empty_player = Player("Toad", "Rocket Star")
print("  expected printed output: Inventory empty")
empty_player.print_inventory()

print("Test 2 - all items unique (each quantity 1)")
p2 = Player("Luigi", "Wild Wiggler")
p2.items = ["shell", "mushroom"]
print("  expected printed output: Inventory: shell: 1, mushroom: 1")
p2.print_inventory()

print("Test 3 - single item repeated many times")
p3 = Player("Bowser", "Standard Kart B")
p3.items = ["banana", "banana", "banana"]
print("  expected printed output: Inventory: banana: 3")
p3.print_inventory()


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
