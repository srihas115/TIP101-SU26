'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 1  ·  Version 3
    Problem 5: Find Leftmost Path II

    If you implemented the previous `left_most()` function iteratively,
    implement it recursively. If you implemented it recursively, implement it
    recursively.

    Evaluate the time complexity of your implementation.

    Write your solution for `left_path` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `left_path` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, value, left=None, right=None):
        pass
def left_path(root):
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

grade(left_path)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 5, 4, 3], expected=[1, 2, 4])   # checks the value your code returns against this example
