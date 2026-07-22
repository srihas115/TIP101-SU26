'''
==============================================================================
    Unit 9: Binary Trees II  ·  Session 2  ·  Version 3
    Problem 4: Print Corner Nodes of Each Level

    Given the `root` of a binary tree, print the value of the corner nodes of
    every level in a binary tree. The corner nodes are the first and last node
    in each level of a binary tree.

    Evaluate the time complexity of your solution. Define your variables and
    give a rationale as to why you believe your solution has the stated time
    complexity.

    Write your solution for `print_corner_nodes` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `print_corner_nodes` and its parameters exactly as given —
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

def print_corner_nodes(root):
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

grade(print_corner_nodes)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([6, 3, 8, 5, None, 4, 2, None, None, 1, 7, None, 3], expected='6\n3\n8\n5\n2\n1\n3')   # checks the printed output against this example
