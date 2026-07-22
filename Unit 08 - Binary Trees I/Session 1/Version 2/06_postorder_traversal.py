'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 1  ·  Version 2
    Problem 6: Post-order Traversal

    Given the `root` of a binary tree, return a list representing the
    postorder traversal of its nodes' values. In an postorder traversal we
    traverse the left subtree, then the right subtree, then the current node.

    Evaluate the time complexity of your function.

    Write your solution for `postorder_traversal` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `postorder_traversal` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, value, left=None, right=None):
        pass
def postorder_traversal(root):
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

grade(postorder_traversal)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5, None, 6], expected=[4, 5, 2, 6, 3, 1])   # checks the value your code returns against this example
