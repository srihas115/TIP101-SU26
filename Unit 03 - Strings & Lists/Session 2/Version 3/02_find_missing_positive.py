'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 3
  Problem 2: Missing Integer

  Write a function `find_missing_positive()` that takes in a *sorted* list
  of integers `nums` that always starts at `1`, and returns the smallest
  missing positive integer.

  Write your solution for `find_missing_positive` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_missing_positive` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_missing_positive(nums):
    pass

nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-element list")
print("  expected:", 2, "| got:", find_missing_positive([1]))

print("Test 2 - missing number right after the first")
print("  expected:", 2, "| got:", find_missing_positive([1,3]))

print("Test 3 - large gap at the end")
print("  expected:", 4, "| got:", find_missing_positive([1,2,3,100]))


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

grade(find_missing_positive)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 5, 6, 10], expected=4)   # checks the value your code returns against this example
