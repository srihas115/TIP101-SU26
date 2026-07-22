'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 2  ·  Version 1
  Problem 9: Divisors

  Write a function `find_divisors()` that takes in an integer `n` as a
  parameter that returns a list of all divisors of `n`.

  Write your solution for `find_divisors` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_divisors` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

lst = find_divisors(6)
print(lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [1,2,3,6], "| got:", find_divisors(6))

print("Test 2 - n is 1 (only divisor is itself)")
print("  expected:", [1], "| got:", find_divisors(1))

print("Test 3 - n is prime")
print("  expected:", [1,7], "| got:", find_divisors(7))

print("Test 4 - n has many divisors")
print("  expected:", [1,2,3,4,6,12], "| got:", find_divisors(12))


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

grade(find_divisors)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(6, expected=[1, 2, 3, 6])   # checks the value your code returns against this example
