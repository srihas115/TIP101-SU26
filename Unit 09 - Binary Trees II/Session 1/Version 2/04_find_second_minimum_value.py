'''
==============================================================================
    Unit 9: Binary Trees II  ·  Session 1  ·  Version 2
    Problem 4: Second Minimum Value

    Given the `root` of a non-empty special binary tree consisting of nodes
    with the non-negative value, where each node in this tree has exactly
    `two` or `zero` children. If the node has two children, then this node's
    value is the smaller value among its two children. More formally, the
    property `root.val = min(root.left.val, root.right.val)` always holds.

    Given such a binary tree, write a function that returns the **second
    minimum** value in the set made of all the nodes' value in the whole tree.

    If no such second minimum value exists, output -1 instead.

    Evaluate the time complexity of the function.

    Write your solution for `find_second_minimum_value` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_second_minimum_value` and its parameters exactly as given —
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

def find_second_minimum_value(root):
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

grade(find_second_minimum_value)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 2, 5, None, None, 5, 7], expected=5)   # checks the value your code returns against this example
