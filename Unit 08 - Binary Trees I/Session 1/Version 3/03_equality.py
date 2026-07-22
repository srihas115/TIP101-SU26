'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 1  ·  Version 3
  Problem 3: 3-Node Equality

  You are given the `root` of a binary tree that has at most `3` nodes: the
  root, its left child, and its right child.

  Return `True` if the root’s children have equal value and `False`
  otherwise.

  Evaluate the time complexity of your function.

  Write your solution for `equality` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `equality` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, value, left=None, right=None):
        pass
def equality(root):
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

grade(equality)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 2], expected=True)   # checks the value your code returns against this example
