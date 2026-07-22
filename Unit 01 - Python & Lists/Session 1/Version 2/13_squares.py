'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 1  ·  Version 2
    Problem 13: Calculate the Squares

    Write a function `squares()` that takes a list of integers `nums` as a
    parameter and returns a new list containing the square of each number in
    the original list.

    Write your solution for `squares` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `squares` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def squares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [1,4,9,16], "| got:", squares([1,2,3,4]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", squares([]))

print("Test 3 - negative numbers")
print("  expected:", [1,4,9], "| got:", squares([-1,-2,-3]))

print("Test 4 - list containing zero")
print("  expected:", [0], "| got:", squares([0]))

print("Test 5 - single-element list")
print("  expected:", [16], "| got:", squares([4]))


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

grade(squares)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=[1, 4, 9, 16])   # checks the value your code returns against this example
