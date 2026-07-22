'''
==============================================================================
  Unit 10: Review  ·  Session 1  ·  Version 1
  Problem 5: Sum Root to Leaf Numbers

  You are given the `root` of a binary tree containing digits from `0` to
  `9` only.

  Each root-to-leaf path in the tree represents a number.

  - For example, the root-to-leaf path `1 -> 2 -> 3` represents the number
  `123`.

  Return *the total sum of all root-to-leaf numbers*.

  A **leaf** node is a node with no children.

  Write your solution for `sum_numbers` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sum_numbers` and its parameters exactly as given —
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



def sum_numbers(root):
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

grade(sum_numbers)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=25)   # checks the value your code returns against this example
