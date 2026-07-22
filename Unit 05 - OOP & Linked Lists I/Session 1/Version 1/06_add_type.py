'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 1
    Problem 6: Add Pokemon Type
    Write your solution in the space provided below, then click ▶ Run to validate it.
    (Full instructions and examples are in the problem set.)

    ⚠️  Keep every class, method, and function name exactly as the problem gives it,
        and use the exact variable names it asks for — the problem set solution validator looks those up
        by name (they're case-sensitive). If it can't find one, the results will tell
        you which name is missing.
==============================================================================
Understand (input, output, core logic):
Adding to list of types

Match:

Plan:
access the types attribute and append with the parameter
'''


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

    def add_type(self, new_type):
        self.types.append(new_type)

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

print()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()


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
