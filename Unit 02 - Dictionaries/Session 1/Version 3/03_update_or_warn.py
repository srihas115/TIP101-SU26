'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 3
  Problem 3: Update or Warn

  Write a function `update_or_warn()` that takes in a dictionary `records`,
  a key `item`, and a new value `update_value` as parameters. The function
  updates the value of `item` in `records` with `update_value` if `item`
  exists. If `item` does not exist, it should print `"<item> not found!"`
  and not modify the dictionary.

  Write your solution for `update_or_warn` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `update_or_warn` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def update_or_warn(records, item, update_value):
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

grade(update_or_warn)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'apple': 1, 'banana': 2, 'orange': 3}, 'grape', 4, expected={'apple': 1, 'banana': 2, 'orange': 3})   # checks the updated first argument against this example
