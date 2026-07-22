'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 1  ·  Version 3
  Problem 3: Path Sum in Binary Tree

  Given the `root` of a binary tree and an integer `target_sum`, return
  `True` if the tree has a **root-to-leaf** path such that adding up all the
  values along the path equals `target_sum`. Return `False` otherwise.

  A **leaf** is a node with no children.

  Evaluate the time complexity of your function.

  Write your solution for `has_path_sum` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `has_path_sum` and its parameters exactly as given —
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



def has_path_sum(root, target_sum):
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

grade(has_path_sum)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1], 22, expected=True)   # checks the value your code returns against this example
