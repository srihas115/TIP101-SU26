'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 1  ·  Version 2
    Problem 10: Calculate Power

    Write a function `power()` that takes in two integers `base` and
    `exponent`. The function should return the value of the base number to the
    power of the `exponent`.

    Write your solution for `power` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `power` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def power(base, exponent):
    res = 1
    for i in range(exponent):
        res *= base
    return res

pow1 = power(2,5)
print(pow1)
pow2 = power(3,3)
print(pow2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - exponent is 0")
print("  expected:", 1, "| got:", power(5, 0))

print("Test 2 - base is 0, positive exponent")
print("  expected:", 0, "| got:", power(0, 3))

print("Test 3 - negative base, even exponent")
print("  expected:", 25, "| got:", power(-5, 2))

print("Test 4 - base is 1")
print("  expected:", 1, "| got:", power(1, 10))

print("Test 5 - exponent is 1")
print("  expected:", 7, "| got:", power(7, 1))


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

grade(power)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(2, 5, expected=32)   # checks the value your code returns against this example
