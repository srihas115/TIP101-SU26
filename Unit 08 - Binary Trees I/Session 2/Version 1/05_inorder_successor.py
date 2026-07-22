'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 2  ·  Version 1
  Problem 5: BST In-order Successor

  In the `remove_bst()` problem, we summarized the in-order successor of a
  given node as the smallest node in the given node’s right subtree. This is
  true if the given node has a right subtree.

  More generally, the in-order successor is the node with the smallest key
  greater than the key of the given node. Given the root of a binary search
  tree, and a `TreeNode` `current`, write a function that returns the in-
  order successor of the `current` node. Assume the tree is balanced.

  Evaluate the time complexity of your solution.

  Write your solution for `inorder_successor` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `inorder_successor` and its parameters exactly as given —
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



def inorder_successor(root, current):
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

grade(inorder_successor)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 5, 15, 1, 8, None, None, None, None, 6, 9], 5, expected=6)   # checks the value your code returns against this example
