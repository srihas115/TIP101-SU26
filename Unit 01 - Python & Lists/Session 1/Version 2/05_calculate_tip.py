'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 5: Calculate Tip

  Write a function `calculate_tip()` that takes in a float `bill` and a
  string `service_quality` as parameters. If `service_quality` is `"poor"`,
  the function should return 10% of the `bill` value. If `service_quality`
  is `"average"`, the function should return 15% of the `bill` value. If
  `service_quality` is `"excellent"`, the function should return 20% of the
  `bill` value. If `service_quality` is any other value, the function should
  return `None`.

  Write your solution for `calculate_tip` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `calculate_tip` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def calculate_tip(bill, service_quality):
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

grade(calculate_tip)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(44.53, 'average', expected=6.6795)   # checks the value your code returns against this example
