'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 1
  Problem 1: Prime Number

  Write a function `is_prime()` that takes in a positive integer `n` and
  returns `True` if it is a prime number and `False` otherwise. A **prime
  number** is a number greater than 1 that has no positive divisors other
  than 1 and itself.

  Write your solution for `is_prime` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_prime` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_prime(n):
    pass

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 1 (not prime by definition)")
print("  expected:", False, "| got:", is_prime(1))

print("Test 2 - n is 2 (smallest prime)")
print("  expected:", True, "| got:", is_prime(2))

print("Test 3 - n is 0")
print("  expected:", False, "| got:", is_prime(0))

print("Test 4 - larger prime")
print("  expected:", True, "| got:", is_prime(17))


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

grade(is_prime)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, expected=True)   # checks the value your code returns against this example
