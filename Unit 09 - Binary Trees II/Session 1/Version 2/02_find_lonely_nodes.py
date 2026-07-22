'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 1  ·  Version 2
  Problem 2: Find Lonely Nodes

  Given the `root` of a binary tree, return a list containing the values of
  all lonely nodes in the tree. Return the list in any order.

  A lonely node is a node that is the only child of its parent node. The
  root of the tree is not lonely because it does not have a parent node.

  Evaluate the time complexity of your function.

  Write your solution for `find_lonely_nodes` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_lonely_nodes` and its parameters exactly as given —
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



def find_lonely_nodes(root):
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

grade(find_lonely_nodes)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, None, 4], expected=[4])   # checks the value your code returns against this example
