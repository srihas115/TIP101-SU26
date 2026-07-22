'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 1  ·  Version 3
  Problem 5: Replace Node Value with Sum of Subtree

  Given a binary tree, in-place replace each node’s value as the sum of all
  elements present in its left and right subtree. You may assume the value
  of an empty child node to be 0.

  Return the root of the modified tree.

  Write your solution for `sum_transform` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sum_transform` and its parameters exactly as given —
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

def sum_transform(root):
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

grade(sum_transform)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, None, 4, 5, 6, None, None, 7, 8], expected=[35, 4, 26, None, 0, 15, 0, None, None, 0, 0])   # checks the value your code returns against this example
