'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 2  ·  Version 2
  Problem 2: Average Score

  Write a function `average()` that takes in a list of integers `scores` as
  a parameter and returns the average score.

  Write your solution for `average` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `average` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def average(scores):
  sum = 0
  for score in scores:
    sum += score
  return sum / len(scores)

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-element list")
print("  expected:", 50.0, "| got:", average([50]))

print("Test 2 - all elements equal")
print("  expected:", 7.0, "| got:", average([7,7,7]))

print("Test 3 - list containing zero")
print("  expected:", 3.0, "| got:", average([0,3,6]))

print("Test 4 - negative numbers")
print("  expected:", -2.0, "| got:", average([-1,-2,-3]))


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

grade(average)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([84, 73, 92, 95, 88], expected=86.4)   # checks the value your code returns against this example
