'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 1  ·  Version 3
  Problem 8: Binary Tree Any Greater

  Given a `value` and the `root` of a binary tree, write a function
  `contains_greater()` which returns `True` if any nodes greater than
  `value` exist in the tree. If no node greater than value exist, return
  `False`. Assume the tree is balanced.

  Evaluate the time complexity of your solution.

  Write your solution for `contains_greater` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `contains_greater` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, value, left=None, right=None):
        pass
def contains_greater(root, value):
    pass


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

grade(contains_greater)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 5, 2, 4, 3], 3, expected=True)   # checks the value your code returns against this example
