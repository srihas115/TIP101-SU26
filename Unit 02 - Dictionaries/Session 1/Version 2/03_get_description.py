'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 3: Dictionary Description

  The following function `get_description()` takes in a dictionary `info`
  and a list `keys` as parameters. For each key in `keys`, the function
  prints the value associated with that key in `info` and prints `None` if
  the key does not exist in `info`.

  However, the function has a bug! Copy the function into your IDE and run
  the code. Work with your group members to find the cause of the bug and
  correctly implement the function.

  Write your solution for `get_description` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `get_description` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def get_description(info, keys):
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

grade(get_description)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'name': 'Tom', 'age': '30', 'occupation': 'engineer'}, ['name', 'occupation', 'salary'], expected='Tom\nengineer\nNone')   # checks the printed output against this example
