'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 1  ·  Version 2
  Problem 5: Transformable by Swapping Subtrees

  Given the roots of two binary trees `root1` and `root2`, write a function
  `can_transform()` that returns `True` if the tree represented by `root1`
  can be converted to the tree represented by `root2` by doing any number of
  swaps of the first tree’s right and left branches.

  Evaluate the time complexity of the function.

  Write your solution for `can_swap` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `can_swap` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def can_swap(root1, root2):
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

grade(can_swap)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([6, 3, 8, 1, 7, 4, 2], [6, 8, 3, 2, 4, 7, 1], expected=True)   # checks the value your code returns against this example
