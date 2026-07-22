'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 2  ·  Version 3
  Problem 3: Cousins in Binary Tree

  Given the `root` of a binary tree with unique values and the values of two
  different nodes of the tree `x` and `y`, return `True` *if the nodes
  corresponding to the values* `x` *and* `y` *in the tree are **cousins**,
  or* `False` *otherwise.*

  Two nodes of a binary tree are **cousins** if they have the same depth
  with different parents.

  Note that in a binary tree, the root node is at the depth `0`, and
  children of each depth `k` node are at the depth `k + 1`.

  Evaluate the time complexity of your solution. Define your variables and
  give a rationale as to why you believe your solution has the stated time
  complexity.

  Write your solution for `is_cousins` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_cousins` and its parameters exactly as given —
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



def is_cousins(root, x, y):
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

grade(is_cousins)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], 4, 3, expected=False)   # checks the value your code returns against this example
