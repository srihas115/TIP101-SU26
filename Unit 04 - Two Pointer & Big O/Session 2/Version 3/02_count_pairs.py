'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 3
  Problem 2: Count Pairs

  Write a function `count_pairs()` that takes in a *0-indexed* list of
  integers `nums` of length `n` and an integer `target` as parameters. The
  function returns the number of index pairs `(i, j)` where `0 <= i < j < n`
  and `nums[i] + nums[j] < target`.

  Write your solution for `count_pairs` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `count_pairs` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_pairs(nums, target):
    pass

nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", count_pairs([], 2))

print("Test 2 - single-element list (no pairs possible)")
print("  expected:", 0, "| got:", count_pairs([5], 2))

print("Test 3 - two-element list, pair qualifies")
print("  expected:", 1, "| got:", count_pairs([1,1], 3))

print("Test 4 - two-element list, pair does not qualify")
print("  expected:", 0, "| got:", count_pairs([5,5], 3))


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

grade(count_pairs)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([-1, 1, 2, 3, 1], 2, expected=3)   # checks the value your code returns against this example
