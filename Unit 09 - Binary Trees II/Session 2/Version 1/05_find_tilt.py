'''
==============================================================================
    Unit 9: Binary Trees II  ·  Session 2  ·  Version 1
    Problem 5: Sum of Node Tilts

    Given the `root` of a binary tree, return the sum of every tree node’s
    tilt. The tilt of a tree node is the absolute difference between the sum
    of all left subtree node values and all right subtree node values. If a
    node does not have a left child, then the sum of the left subtree node
    values is treated as `0`. The rule is similar if the node does not have a
    right child.

    Evaluate the time complexity of your solution. Define your variables and
    give a rationale as to why you believe your solution has the stated time
    complexity.

    Write your solution for `find_tilt` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_tilt` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def find_tilt(root):
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

grade(find_tilt)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=1)   # checks the value your code returns against this example
