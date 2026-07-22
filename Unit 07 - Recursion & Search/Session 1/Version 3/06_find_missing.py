'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 3
    Problem 6: Find Missing

    Given a sorted list of integers `nums` containing `n` distinct numbers in
    the range `[0, n]`, return the only number in the range that is missing
    from the list.

    Your solution must have `O(log n)` time complexity.

    Write your solution for `find_missing` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_missing` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_missing(nums):
    pass

# Example Input: nums = [0,1,3]


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

grade(find_missing)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([0, 1, 3], expected=2)   # checks the value your code returns against this example
