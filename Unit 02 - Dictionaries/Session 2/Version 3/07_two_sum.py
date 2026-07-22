'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 2  ·  Version 3
    Problem 7: Target Sum

    Write a function `two_sum()` that takes in a list of integers `nums` and
    an integer `target` as parameters. The function should return the indices
    of the two numbers that add up to `target`. You may assume that each input
    would have exactly **one** solution and you may not use the same element
    twice. The function can return the indices in any order.

    Write your solution for `two_sum` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `two_sum` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def two_sum(nums, target):
    pass

nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)

print(q_1)
print(q_2)
print(q_3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - two-element list, exact match")
print("  expected:", [0, 1], "| got:", two_sum([4, 5], 9))

print("Test 2 - negative numbers")
print("  expected:", [0, 1], "| got:", two_sum([-3, -1], -4))

print("Test 3 - target requires the last two elements")
print("  expected:", [2, 3], "| got:", two_sum([1, 2, 3, 4], 7))


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

grade(two_sum)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 7, 11, 15], 9, expected=[0, 1])   # checks the value your code returns against this example
