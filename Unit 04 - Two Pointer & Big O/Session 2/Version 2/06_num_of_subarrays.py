'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 2
    Problem 6: Greater Than Threshold

    Write a function `num_of_subarrays()` that takes in a list of integers
    `nums` and two integers `k` and `threshold` as parameters. The function
    returns the number of `subarrays` of size `k` whose average is greater
    than or equal to `threshold`.

    Write your solution for `num_of_subarrays` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `num_of_subarrays` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def num_of_subarrays(lst, k, threshold):
    pass

nums = [2,2,2,2,5,5,5,8]
count = num_of_subarrays(nums, 3, 4)
print(count)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no qualifying subarrays")
print("  expected:", 0, "| got:", num_of_subarrays([1,1,1], 2, 5))

print("Test 2 - all subarrays qualify")
print("  expected:", 3, "| got:", num_of_subarrays([10,10,10,10], 2, 5))

print("Test 3 - k equals the length of the list (single subarray checked)")
print("  expected:", 1, "| got:", num_of_subarrays([5,5,5], 3, 4))


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

grade(num_of_subarrays)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 2, 2, 2, 5, 5, 5, 8], 3, 4, expected=3)   # checks the value your code returns against this example
