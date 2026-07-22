'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 2  ·  Version 2
  Problem 5: BST In-order Predecessor

  In the `remove_bst()` problem, we summarized the in-order predecessor of a
  given node as the largest node in the given node’s left subtree. This is
  true if the given node has a left subtree.

  More generally, the in-order predecessor is the node with the largest key
  *less* *than* the key of the given node. Given the `root` of a binary
  search tree, and a `TreeNode` `current`, write a function that returns the
  in-order predecessor of the `current` node. Assume the tree is balanced.

  Evaluate the time complexity of your solution.

  Write your solution for `inorder_predecessor` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `inorder_predecessor` and its parameters exactly as given —
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



def inorder_predecessor(root, current):
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

grade(inorder_predecessor)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 5, 15, 2, 8, None, None, 1, 3], 5, expected=3)   # checks the value your code returns against this example
