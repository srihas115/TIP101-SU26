'''
==============================================================================
  Unit 10: Review  ·  Session 2  ·  Version 3
  Problem 4: Leaves of a Binary Tree

  Given the `root` of a binary tree, collect a tree's nodes as if you were
  doing this:

  - Collect all the leaf nodes. - Remove all the leaf nodes. - Repeat until
  the tree is empty.

  Write your solution for `find_leaves` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_leaves` and its parameters exactly as given —
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

def find_leaves(root):
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
from problem_set_solution_validator import grade

grade(find_leaves)   # ▶ Run this file to validate your solution
