'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 1
  Problem 5: Choose Pokemon
  Write your solution in the space provided below, then click ▶ Run to validate it.
  (Full instructions and examples are in the problem set.)

  ⚠️  Keep every class, method, and function name exactly as the problem gives it,
      and use the exact variable names it asks for — the problem set solution validator looks those up
      by name (they're case-sensitive). If it can't find one, the results will tell
      you which name is missing.
==============================================================================
'''


# UPI
# Understand: Check the value of is_caught and print output depending on value
# Plan: use an if conditional on the is_caught variable to determine if the print is needed
# Implement: (below)
class Pokemon():
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
        
    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()


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

grade(Pokemon)   # ▶ Run this file to validate your work
