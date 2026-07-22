'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 3
  Problem 4: Sorted Squares

  Write a function `sorted_squares()` that takes in an integer list `nums`
  that is *sorted* in non-decreasing order. The function returns a list of
  the squares of each number also sorted in non-decreasing order.

  Write your solution for `sorted_squares` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sorted_squares` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sorted_squares(nums):
    pass

nums = [1,2,3,4]
sq_nums = sorted_squares(nums)
print(sq_nums)
nums2 = [-4,-1,0,3,10]
sq_nums2 = sorted_squares(nums2)
print(sq_nums2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", sorted_squares([]))

print("Test 2 - single-element list")
print("  expected:", [16], "| got:", sorted_squares([-4]))

print("Test 3 - all negative numbers")
print("  expected:", [1,4,9], "| got:", sorted_squares([-3,-2,-1]))

print("Test 4 - all zeros")
print("  expected:", [0,0,0], "| got:", sorted_squares([0,0,0]))


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

grade(sorted_squares)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=[1, 4, 9, 16])   # checks the value your code returns against this example
