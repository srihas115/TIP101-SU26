'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 12: Calculate Factorial

  Write a function `factorial()` that takes in an integer `n` as a parameter
  and returns its factorial. The factorial of a number is the product of all
  positive integers less than or equal to that number. For example, the
  factorial of 5 (*denoted as 5!*) is 5! = 5 * 4 * 3 * 2 * 1 which equals
  120.

  Write your solution for `factorial` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `factorial` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def factorial(n):
    res = 1
    for num in range(n, 0, -1):
        res *= num
    return res

print(factorial(3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 0 (0! is 1)")
print("  expected:", 1, "| got:", factorial(0))

print("Test 2 - n is 1")
print("  expected:", 1, "| got:", factorial(1))

print("Test 3 - n is 5")
print("  expected:", 120, "| got:", factorial(5))


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

grade(factorial)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(3, expected=6)   # checks the value your code returns against this example
