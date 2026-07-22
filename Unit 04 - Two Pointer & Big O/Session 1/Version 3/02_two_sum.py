'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 3
  Problem 2: Two-Pointer Target Sum

  Write a function `two_sum()` that takes in a *sorted* list of integers
  `nums` and an integer `target` as parameters and returns the indices of
  the two numbers that add up to `target`. You may assume that each input
  would have exactly one solution, and you may not use the same element
  twice. You can return the indices in any order.

  The function must use the **two-pointer approach**, which is a common
  technique in which we initialize two variables (also called a pointer in
  this context) to track different indices or places in a list or string,
  then moves the pointers to point at new indices based on certain
  conditions. In the most common variation of the two-pointer approach, we
  initialize one variable to point at the beginning of a list and a second
  variable/pointer to point at the end of list. We then shift the pointers
  to move inwards through the list towards each other, until our problem is
  solved or the pointers reach the opposite ends of the list.

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

nums = [2,7,11,15,17]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - two-element list, exact sum")
print("  expected:", [0, 1], "| got:", two_sum([4, 5], 9))

print("Test 2 - negative numbers in sorted list")
print("  expected:", [0, 1], "| got:", two_sum([-4, -1], -5))

print("Test 3 - target requires the first and last elements")
print("  expected:", [0, 3], "| got:", two_sum([1, 2, 3, 9], 10))


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
# test([2, 7, 11, 15, 17], 9, expected=[0, 1])   # checks the value your code returns against this example
