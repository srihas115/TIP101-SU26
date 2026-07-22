'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 1  ·  Version 1
    Problem 14: Total Sum in Range

    Write a function `sum_range()` that returns the sum of numbers from a
    given `start` value to a given `stop` value (inclusive).

    Write your solution for `sum_range` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `sum_range` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sum_range(start, stop):
    sum = 0
    for i in range(start, stop+1):
        sum += i
    return sum

sum = sum_range(3, 9)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - start=3, stop=9 (matches example)")
print("  expected:", 42, "| got:", sum_range(3,9))

print("Test 2 - start equals stop (single number range)")
print("  expected:", 5, "| got:", sum_range(5,5))

print("Test 3 - start greater than stop (empty range)")
print("  expected:", 0, "| got:", sum_range(9,3))

print("Test 4 - negative range")
print("  expected:", -6, "| got:", sum_range(-3,-1))


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

grade(sum_range)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(3, 9, expected=42)   # checks the value your code returns against this example
