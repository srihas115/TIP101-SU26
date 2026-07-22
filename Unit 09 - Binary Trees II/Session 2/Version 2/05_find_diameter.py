'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 2  ·  Version 2
  Problem 5: Diameter of Binary Tree

  Given the `root` of a binary tree, return the *length of the **diameter**
  of the tree.*

  The **diameter** of a binary tree is the **length** of the longest path
  between any two nodes in a tree. This path may or may not pass through the
  `root`.

  The **length** of a path between two nodes is represented by the number of
  edges between them.

  Write your solution for `find_diameter` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_diameter` and its parameters exactly as given —
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

def find_diameter(root):
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

grade(find_diameter)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], expected=3)   # checks the value your code returns against this example
