'''
==============================================================================
    Unit 9: Binary Trees II  ·  Session 2  ·  Version 3
    Problem 2: Node Values Between Given Levels

    Given the `root` of a binary tree, return a list of all the node values
    between to given levels `start_level` and `end_level` in a binary tree.

    You may assume `1 <= start_level <= end_level <= tree depth`.

    Evaluate the time complexity of your solution. Define your variables and
    give a rationale as to why you believe your solution has the stated time
    complexity.

    Write your solution for `get_level_range` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `get_level_range` and its parameters exactly as given —
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

def get_level_range(root, start_level, end_level):
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

grade(get_level_range)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 2, 4, expected=[5, 1, 6, 2, 0, 8, 7, 4])   # checks the value your code returns against this example
