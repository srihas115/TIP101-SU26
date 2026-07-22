'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 1  ·  Version 3
  Problem 1: Choose Your Pokemon

  Copy and paste the following function:

  Write your solution for `choose_pokemon` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `choose_pokemon` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def choose_pokemon(my_pokemon):
    pass  # replace this line with your solution













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
