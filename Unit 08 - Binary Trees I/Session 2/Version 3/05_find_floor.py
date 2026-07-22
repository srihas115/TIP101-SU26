'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 2  ·  Version 3
  Problem 5: BST Find Floor

  Given a `value` and the `root` of a binary search tree, write a function
  `find_floor()` that finds the largest value in the binary search tree less
  than or equal to the given value. If no such node exists, return `None`.
  Assume the tree is balanced.

  Evaluate the time complexity of your solution.

  Write your solution for `find_floor` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_floor` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def find_floor(root, value):
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

grade(find_floor)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([8, 4, 12, 2, 6, 10, 14], 7, expected=6)   # checks the value your code returns against this example
