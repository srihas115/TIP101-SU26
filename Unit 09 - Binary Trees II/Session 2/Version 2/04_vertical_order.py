'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 2  ·  Version 2
  Problem 4: Vertical Order Traversal

  Given the `root` of a binary tree, return the vertical order traversal of
  its nodes’ values. (i.e., from top to bottom, column by column). If two
  nodes are in the same row and column, the order should be from left to
  right.

  Evaluate the time complexity of your solution. Define your variables and
  give a rationale as to why you believe your solution has the stated time
  complexity.

  Write your solution for `vertical_order` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `vertical_order` and its parameters exactly as given —
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



def vertical_order(root):
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

grade(vertical_order)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 9, 20, None, None, 15, 7], expected=[[9], [3, 15], [20], [7]])   # checks the value your code returns against this example
