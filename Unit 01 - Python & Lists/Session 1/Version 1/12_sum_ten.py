'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 1
  Problem 12: Sum of 1 to 10

  Write a function `sum_ten()` that returns the sum of numbers from 1 to 10.

  Write your solution for `sum_ten` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sum_ten` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sum_ten():
    sum = 0
    for i in range(1,11):
        sum += i
    return sum

output = sum_ten()

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - basic call")
print("  expected:", 55, "| got:", sum_ten())

print("Test 2 - calling again returns the same result")
print("  expected:", 55, "| got:", sum_ten())


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade

grade(sum_ten)   # ▶ Run this file to validate your solution
