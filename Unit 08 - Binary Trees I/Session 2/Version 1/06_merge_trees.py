'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 2  ·  Version 1
  Problem 6: Merge Binary Trees

  You are given two binary trees with roots root1 and root2.

  Imagine that when you put one of them to cover the other, some nodes of
  the two trees are overlapped while the others are not. You need to merge
  the two trees into a new binary tree. The merge rule is that if two nodes
  overlap, then sum node values up as the new value of the merged node.
  Otherwise, the NOT null node will be used as the node of the new tree.

  Return *the merged tree*.

  Write your solution for `merge_trees` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `merge_trees` and its parameters exactly as given —
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



def merge_trees(root1, root2):
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

grade(merge_trees)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], expected=[3, 4, 5, 5, 4, None, 7])   # checks the value your code returns against this example
