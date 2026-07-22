'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 1
  Problem 15: Negative Numbers

  Write a function `print_negatives()` that takes a list of integers `lst`
  and prints all negative numbers in the list.

  Write your solution for `print_negatives` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `print_negatives` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def print_negatives(lst):
    for num in lst:
        if num < 0:
            print(num)

print_negatives([3,-2,2,1,-5])

print_negatives([1,2,3,4,5])

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_negatives([])

print("Test 2 - single negative element")
print("  expected printed output: -4")
print_negatives([-4])

print("Test 3 - single positive element (nothing printed)")
print("  expected printed output: (nothing)")
print_negatives([7])

print("Test 4 - all negative numbers")
print("  expected printed output: -1 / -2 / -3")
print_negatives([-1,-2,-3])


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

grade(print_negatives)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, -2, 2, 1, -5], expected='-2\n-5')   # checks the printed output against this example
