'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 1  ·  Version 1
  Problem 4: Increasing Order Search Tree

  Given the `root` of a binary search tree, rearrange the tree in in-order
  so that the leftmost node of the tree is now the root of tree and every
  node has no left child and only one right child.

  Return the root of the modified tree

  Evaluate the time complexity of your function.

  Write your solution for `increasing_bst` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `increasing_bst` and its parameters exactly as given —
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

def increasing_bst(root):
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

grade(increasing_bst)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 1, 7], expected=[1, None, 5, None, 7])   # checks the value your code returns against this example
