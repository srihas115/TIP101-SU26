'''
==============================================================================
    Unit 9: Binary Trees II  ·  Session 1  ·  Version 3
    Problem 2: Find Corresponding Node in Cloned Tree

    You are given the `roots` of two binary trees, `original` and `cloned`.
    You are also give a `TreeNode` `target` which is a reference to a node in
    the `original` tree.

    The cloned `tree` is a copy of the `original` tree.

    Return a reference to the same node as `target` in the `cloned` tree.

    You may not change any of the two trees or the `target node`. The answer
    must be a reference to a node in the cloned tree.

    Evaluate the time complexity of your function.

    Write your solution for `get_target_copy` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `get_target_copy` and its parameters exactly as given —
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


def get_target_copy(original, cloned, target):
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

grade(get_target_copy)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([7, 4, 3, None, None, 6, 19], None, 3, expected=3)   # checks the value your code returns against this example
