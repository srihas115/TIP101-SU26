'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 1  ·  Version 2
    Problem 8: Binary Tree Is Leaf

    Given a `value` and the `root` of a binary search tree, write a function
    `is_leaf_bst()` that returns `True` if a node with the given value is a
    leaf node and `False` otherwise. Assume the tree is balanced.

    Evaluate the time complexity of your solution.

    Write your solution for `is_leaf` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_leaf` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, value, left=None, right=None):
        pass
def is_leaf(root, value):
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

grade(is_leaf)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 5, 4, 3], 5, expected=True)   # checks the value your code returns against this example
