'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 1  ·  Version 2
    Problem 3: 3-Node Product II

    Given the `root` of a binary tree that has at most `3` nodes: the root,
    its left child, and its right child, return `True` if the value of the
    root is equal to the product of the values of its two children. Return
    `False` otherwise. If the `root` has only one child, return `False`.

    Evaluate the time complexity of your function.

    Write your solution for `check_tree` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `check_tree` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, value, left=None, right=None):
        pass
def check_tree(root):
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

grade(check_tree)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 2, 5], expected=True)   # checks the value your code returns against this example
