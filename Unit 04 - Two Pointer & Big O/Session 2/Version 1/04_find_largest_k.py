'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 1
    Problem 4: Positive Negative Pairs

    Write a function `find_largest_k()` that takes in a list of integers
    `nums` that does not contain any zeroes as a parameter. The function finds
    the **largest positive** integer `k` such that `-k` also exists in the
    array and returns `k`. If there is no such integer, return `-1`.

    Write your solution for `find_largest_k` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_largest_k` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_largest_k(nums):
    pass

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no valid pair")
print("  expected:", -1, "| got:", find_largest_k([1,2,3]))

print("Test 2 - empty list")
print("  expected:", -1, "| got:", find_largest_k([]))

print("Test 3 - single pair only")
print("  expected:", 5, "| got:", find_largest_k([5,-5]))

print("Test 4 - multiple pairs, picks the largest")
print("  expected:", 3, "| got:", find_largest_k([1,-1,2,-2,3,-3]))


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

grade(find_largest_k)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([-1, 2, -3, 3, -1], expected=3)   # checks the value your code returns against this example
