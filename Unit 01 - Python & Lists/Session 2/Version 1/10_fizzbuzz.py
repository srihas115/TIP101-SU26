'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 2  ·  Version 1
  Problem 10: FizzBuzz

  Write a function `fizzbuzz()` that takes in an integer `n` as a parameter
  and prints the numbers from 1 to `n`. For multiples of 3, print `"Fizz"`
  instead of the number. For multiples of 5, print `"Buzz"` instead of the
  number.

  Write your solution for `fizzbuzz` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `fizzbuzz` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def fizzbuzz(n):
    if n == 0:
        return
    
    for i in range(1, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(13)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 1 (prints just 1)")
print("  expected printed output: 1")
fizzbuzz(1)

print("Test 2 - n is 3 (last value is a multiple of 3)")
print("  expected printed output: 1 / 2 / Fizz")
fizzbuzz(3)

print("Test 3 - n is 5 (last value is a multiple of 5)")
print("  expected printed output: 1 / 2 / Fizz / 4 / Buzz")
fizzbuzz(5)

print("Test 4 - n is 0 (nothing printed)")
print("  expected printed output: (nothing)")
fizzbuzz(0)


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

grade(fizzbuzz)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(13, expected='1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13')   # checks the printed output against this example
