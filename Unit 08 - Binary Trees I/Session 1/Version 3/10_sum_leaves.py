'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 1  ·  Version 3
  Problem 10: BST Leaves Sum to Root

  Given the `root` of a binary tree, write a function `leaf_sum()` that
  returns `True` if the sum of the values of all the leaves equal the sum of
  the value of the root. Return `False` otherwise.

  Evaluate the time complexity of your function

  Write your solution for `sum_leaves` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sum_leaves` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, value, left=None, right=None):
        pass
def sum_leaves(root):
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

grade(sum_leaves)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, None, 1, 3], expected=True)   # checks the value your code returns against this example
