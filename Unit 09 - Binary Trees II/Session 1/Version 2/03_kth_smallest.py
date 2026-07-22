'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 1  ·  Version 2
  Problem 3: Kth Smallest in BST

  Given the `root` of a binary search tree and a positive integer `k`,
  return the value of the `kth` smallest node in the tree. All nodes in the
  tree are guaranteed to be unique.

  Evaluate the time complexity of your function.

  Write your solution for `kth_smallest` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `kth_smallest` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def kth_smallest(root, k):
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

grade(kth_smallest)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([15, 10, 20, 8, 12, 16, 26], 4, expected=15)   # checks the value your code returns against this example
