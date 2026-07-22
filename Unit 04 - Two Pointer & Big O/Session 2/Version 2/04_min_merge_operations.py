'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 2
    Problem 4: Merge to Palindrome

    Write a function `min_merge_operations()` that takes in a list of non-
    negative integers `nums` and returns the minimum number of merge
    operations to make it a palindrome. A merge operation is adding two of the
    integers.

    Write your solution for `min_merge_operations` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `min_merge_operations` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def min_merge_operations(nums):
    pass

nums = [6,1,3,7]
print(min_merge_operations(nums))

nums2 = [1,3,3,1]
print(min_merge_operations(nums2))

nums3 = [1,3,2,7]
print(min_merge_operations(nums3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-element list (trivially a palindrome)")
print("  expected:", 0, "| got:", min_merge_operations([9]))

print("Test 2 - two-element list, already equal")
print("  expected:", 0, "| got:", min_merge_operations([5,5]))

print("Test 3 - two-element list, different values (one merge needed)")
print("  expected:", 1, "| got:", min_merge_operations([3,7]))


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

grade(min_merge_operations)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([6, 1, 3, 7], expected=1)   # checks the value your code returns against this example
