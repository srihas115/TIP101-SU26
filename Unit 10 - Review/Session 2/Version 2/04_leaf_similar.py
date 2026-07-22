'''
==============================================================================
  Unit 10: Review  ·  Session 2  ·  Version 2
  Problem 4: Leaf-Similar Trees

  Consider all the leaves of a binary tree, from left to right order, the
  values of those leaves form a **leaf value sequence.**

  Write your solution for `leaf_similar` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `leaf_similar` and its parameters exactly as given —
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

def leaf_similar(root1, root2):
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

grade(leaf_similar)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, None, None, None, None, 9, 8], expected=False)   # checks the value your code returns against this example
