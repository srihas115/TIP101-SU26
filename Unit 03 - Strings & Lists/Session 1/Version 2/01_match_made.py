'''
==============================================================================
    Unit 3: Strings & Lists  ·  Session 1  ·  Version 2
    Problem 1: Perfect Match

    Copy and paste the following function:

    Write your solution for `match_made` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `match_made` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def match_made(dictionary):
    for key, value in dictionary.items():
        print( f"{key} and {value} are a perfect match.")


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

grade(match_made)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'Peanut butter': 'Jelly', 'Spongebob': 'Patrick', 'Ash': 'Pikachu'}, expected='Peanut butter and Jelly are a perfect match.\nSpongebob and Patrick are a perfect match.\nAsh and Pikachu are a perfect match.')   # checks the printed output against this example
