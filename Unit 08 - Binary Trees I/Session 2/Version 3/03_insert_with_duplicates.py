'''
==============================================================================
  Unit 8: Binary Trees I  ·  Session 2  ·  Version 3
  Problem 3: BST Insert III (duplicates left)

  Given the `root` of a binary search tree, insert a new node with a given
  `value` into the tree. Return the `root` of the modified tree. If a node
  with the given value already exists, place the new node in the left
  subtree. You do not need to maintain a balanced tree.

  Evaluate the time complexity of your function.

  Write your solution for `insert_with_duplicates` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `insert_with_duplicates` and its parameters exactly as given —
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



def insert_with_duplicates(root, value):
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

grade(insert_with_duplicates)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 8, 15, 1, 6], 9, expected=[10, 8, 15, 1, 6, None, None, None, None, None, 9])   # checks the value your code returns against this example
