'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 8: Quality Control

  Write a function `quality_control()` that takes in a dictionary
  `product_scores` and an integer `threshold` as parameters. The dictionary
  `product_scores` has key-value pairs that represent a product ID and its
  quality rating. If the product has a score greater than or equal to
  `threshold`, the function categorizes it as a `"pass"`. If the product has
  a score less than `threshold`, the function categorizes it as a `"fail"`.
  The function returns a new dictionary where the key-value pair is the
  product ID and whether it is a `"pass"` or `"fail"`.

  Write your solution for `quality_control` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `quality_control` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def quality_control(product_scores, threshold):
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

grade(quality_control)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'x0123': 75, 'x0124': 40, 'x0125': 90, 'x0126': 55}, 60, expected={'x0123': 'pass', 'x0124': 'fail', 'x0125': 'pass', 'x0126': 'fail'})   # checks the value your code returns against this example
