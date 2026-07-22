'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 8: Above the Threshold

  Write a function `above_threshold()` that takes in a list of integers
  `lst` and an integer `threshold` as parameters. The function should
  iterate through the original list and return a new list containing only
  numbers that are greater than `threshold`.

  Write your solution for `above_threshold` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `above_threshold` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def above_threshold(lst, threshold):
    res = []
    for num in lst:
        if num > threshold:
            res.append(num)
    return res

lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", above_threshold([], 5))

print("Test 2 - single-element list above threshold")
print("  expected:", [7], "| got:", above_threshold([7], 5))

print("Test 3 - single-element list equal to threshold (excluded, not > threshold)")
print("  expected:", [], "| got:", above_threshold([5], 5))

print("Test 4 - negative numbers with negative threshold")
print("  expected:", [-1, -5], "| got:", above_threshold([-1,-5,-10], -6))

print("Test 5 - unsorted list, order preserved")
print("  expected:", [9, 8], "| got:", above_threshold([1,9,3,8,2], 4))


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

grade(above_threshold)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([8, 2, 13, 11, 4, 10, 14], 10, expected=[13, 11, 14])   # checks the value your code returns against this example
