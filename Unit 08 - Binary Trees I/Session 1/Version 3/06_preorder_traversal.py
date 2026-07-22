'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 1  ·  Version 3
  Problem 6: Pre-order Traversal

  Given the `root` of a binary tree, return a list representing the preorder
  traversal of its nodes' values. In a preorder traversal we traverse the
  current node, then the left subtree, then the right subtree.

  Write your solution for `preorder_traversal` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `preorder_traversal` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, value, left=None, right=None):
        pass
def preorder_traversal(root):
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

grade(preorder_traversal)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 5, 4, 3], expected=[1, 2, 4, 3, 5])   # checks the value your code returns against this example
