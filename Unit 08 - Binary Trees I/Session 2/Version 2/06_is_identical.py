'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 2  ·  Version 2
    Problem 6: Identical Binary Trees

    Given the roots of two binary trees `root1` and `root2`, write a function
    that returns `True` if they are identical and `False` otherwise. Two
    binary trees are considered the same if they are structurally identical
    and the nodes have the same values.

    Write your solution for `is_identical` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_identical` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_identical(root1, root2):
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

grade(is_identical)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], [1, 2, 3], expected=True)   # checks the value your code returns against this example
