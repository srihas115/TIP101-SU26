def choose_pokemon(my_pokemon):
    for pokemon in my_pokemon:
        print(f"{pokemon} I choose you!")


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade, test

grade(choose_pokemon)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['Pikachu', 'Charizard', 'Eevee'], expected='Pikachu I choose you!\nCharizard I choose you!\nEevee I choose you!')   # checks the printed output against this example
