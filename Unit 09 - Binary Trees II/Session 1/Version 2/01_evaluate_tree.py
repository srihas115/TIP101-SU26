'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 1  ·  Version 2
  Problem 1: Evaluate Boolean Full Binary Tree

  You are given the `root` of a **full binary tree** with the following
  properties:

  - **Leaf nodes** have either the boolean value `True` or `False` . -
  **Non-leaf nodes** have either the string value `OR` or `AND`.

  The **evaluation** of a node is as follows:

  - If the node is a leaf node, the evaluation is the **value** of the node,
  i.e. `True` or `False`. - Otherwise, **evaluate** the node's two children
  and **apply** the boolean operation of its value with the children's
  evaluations.

  Return *result of **evaluating** the* `root` *node.* Return the result of
  evaluating the root nod

  A **full binary tree** is a binary tree where each node has either `0` or
  `2` children.

  A **leaf node** is a node that has zero children.

  Evaluate the time complexity of your function.

  Write your solution for `evaluate_tree` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `evaluate_tree` and its parameters exactly as given —
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

def evaluate_tree(root):
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

grade(evaluate_tree)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['OR', True, 'AND', None, None, False, True], expected=True)   # checks the value your code returns against this example
