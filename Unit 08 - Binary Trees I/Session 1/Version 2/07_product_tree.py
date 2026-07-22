'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 1  ·  Version 2
  Problem 7: Binary Tree Product

  Given the `root` of a binary tree, write a function that returns the
  product of all nodes’ values in a binary tree. If the tree is empty,
  return `1`.

  Evaluate the time complexity of your function.

  Write your solution for `product_tree` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `product_tree` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, value, left=None, right=None):
        pass
def product_tree(root):
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

grade(product_tree)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, 5, 1, 3], expected=120)   # checks the value your code returns against this example
