'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 2  ·  Version 1
    Problem 4: Count Rotations

    You are given a circularly sorted list of integers. A circularly sorted
    list of integers is a sorted list whose elements have then been rotated
    some number of times such that the last element of the array becomes the
    first element of the array. Write a function `count_rotations()` that
    returns the total number of times the array is rotated. Assume there are
    no duplicates in the array.

    Write your solution for `count_rotations` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `count_rotations` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_rotations(nums):
    pass

# Example Input: [8, 9, 10, 2, 5, 6]


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

grade(count_rotations)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([8, 9, 10, 2, 5, 6], expected=3)   # checks the value your code returns against this example
