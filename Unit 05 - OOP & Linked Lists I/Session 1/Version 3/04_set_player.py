'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 3
    Problem 4: Set Character
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

    def set_player(self, name):
        pass

player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Mario", "Standard Kart M")
player_one.set_player("Peach")
player_two.set_player("Kermit")

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - valid character name")
p1 = Player("Yoshi", "Super Blooper")
print("  expected printed output: Character updated")
p1.set_player("Mario")
print("  expected character after:", "Mario", "| got:", p1.character)

print("Test 2 - invalid character name (unchanged)")
p2 = Player("Yoshi", "Super Blooper")
print("  expected printed output: Invalid character")
p2.set_player("Kermit")
print("  expected character after:", "Yoshi", "| got:", p2.character)

print("Test 3 - valid character name (Bowser)")
p3 = Player("Toad", "Rocket Star")
print("  expected printed output: Character updated")
p3.set_player("Bowser")
print("  expected character after:", "Bowser", "| got:", p3.character)


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
