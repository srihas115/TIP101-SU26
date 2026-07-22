'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 2  ·  Version 2
  Problem 3: Increment by 1

  Write a function `increment_values()` that takes in a list of integers
  `lst` as a parameter and returns a new list containing each element
  incremented by 1.

  Write your solution for `increment_values` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `increment_values` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def increment_values(lst):
    pass

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", increment_values([]))

print("Test 2 - negative numbers")
print("  expected:", [0, -1], "| got:", increment_values([-1,-2]))

print("Test 3 - list containing zero")
print("  expected:", [1], "| got:", increment_values([0]))

print("Test 4 - single-element list")
print("  expected:", [11], "| got:", increment_values([10]))


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

grade(increment_values)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 5, 8, 2], expected=[4, 6, 9, 3])   # checks the value your code returns against this example
