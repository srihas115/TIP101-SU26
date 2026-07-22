'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 2  ·  Version 3
  Problem 1: Level Order Traversal in a Dictionary

  Given the following pseudocode and the `root` of a binary tree, return a
  dictionary storing the level order traversal of it’s nodes’ values (i.e.,
  from left to right, level by level).

  The dictionary’s key should be an integer representing the level. The
  corresponding value for each key should be a list of node values in that
  level from left to right.

  Evaluate the time complexity of your solution. Define your variables and
  give a rationale as to why you believe your solution has the stated time
  complexity.

  Write your solution for `level_dict` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `level_dict` and its parameters exactly as given —
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



def level_dict(root):
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

grade(level_dict)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, 6, 1, 3], expected={1: [4], 2: [2, 6], 3: [1, 3]})   # checks the value your code returns against this example
