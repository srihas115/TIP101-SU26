'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 1  ·  Version 1
    Problem 10: BST Descending Leaves

    Given the `root` of a binary search tree, write a function
    `descending_leaves()` that returns a list of the values of all leaves in
    the BST in descending order. Assume the tree is balanced.

    <!-- **ADD HINT: Leaves** -->

    Write your solution for `descending_leaves` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `descending_leaves` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def descending_leaves(root):
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

grade(descending_leaves)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, 5, 1, 3], expected=[5, 3, 1])   # checks the value your code returns against this example
