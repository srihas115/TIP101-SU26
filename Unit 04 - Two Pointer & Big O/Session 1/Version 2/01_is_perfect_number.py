'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 2
    Problem 1: Perfect Number

    Write a function `is_perfect_number()` that takes in a positive integer
    `n` and returns `True` if it is a perfect number and `False` otherwise. A
    **perfect number** is a positive integer that is equal to the sum of its
    proper divisors, excluding itself.

    For example, 6 is a perfect number because its divisors or 1, 2, and 3 and
    1 + 2 + 3 = 6.

    Write your solution for `is_perfect_number` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_perfect_number` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_perfect_number(n):
    pass

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 1 (no proper divisors sum to itself)")
print("  expected:", False, "| got:", is_perfect_number(1))

print("Test 2 - next known perfect number")
print("  expected:", True, "| got:", is_perfect_number(496))

print("Test 3 - non-perfect number")
print("  expected:", False, "| got:", is_perfect_number(10))


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

grade(is_perfect_number)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(6, expected=True)   # checks the value your code returns against this example
