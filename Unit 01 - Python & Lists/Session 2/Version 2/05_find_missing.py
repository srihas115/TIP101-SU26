'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 2
    Problem 5: Missing Number

    Write a function `find_missing()` that takes in a list `nums` containing
    `n` unique numbers in the range `[0,n]`. The function returns the only
    number in the range that is missing from the list.

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

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - missing number is 0")
print("  expected:", 0, "| got:", find_missing([1]))

print("Test 2 - missing number is the largest value n")
print("  expected:", 1, "| got:", find_missing([0]))

print("Test 3 - missing number is the last in a longer range")
print("  expected:", 3, "| got:", find_missing([0,1,2]))

print("Test 4 - missing number is in the middle")
print("  expected:", 2, "| got:", find_missing([3,0,1]))


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
# test([2, 4, 1, 0, 5], expected=3)   # checks the value your code returns against this example
