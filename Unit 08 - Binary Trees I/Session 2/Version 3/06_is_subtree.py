'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 2  ·  Version 3
  Problem 6: Nested Binary Trees (is_subtree)

  Given the roots of two binary trees `root` and `sub_root`, return `True`
  if there is a subtree of `root` with the same structure and node values of
  `sub_root` and `False` otherwise.

  A subtree of a binary tree is a tree that consists of a node in and all of
  this node's descendants. The tree could also be considered as a subtree of
  itself.

  Evaluate the time complexity of your solution.

  Write your solution for `is_subtree` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_subtree` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_subtree(root, sub_root):
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

grade(is_subtree)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 3, 5, 6, 7, None, 12], [3, 6, 7], expected=True)   # checks the value your code returns against this example
