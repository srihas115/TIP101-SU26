'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 2
    Problem 9: Create Number

    Write a function `list_to_number()` that takes in a list `digits` where
    each item is a digit between 0-9. The function returns the number they
    represent when combined.

    Write your solution for `list_to_number` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `list_to_number` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def list_to_number(digits):
    num = 0
    multiplier = 1
    for i in range(len(digits)-1, -1, -1):
        num += digits[i] * multiplier
        multiplier *= 10
    return num

digits = [1,0,3]
number = list_to_number(digits)
print(number)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single digit")
print("  expected:", 7, "| got:", list_to_number([7]))

print("Test 2 - leading zero digit")
print("  expected:", 5, "| got:", list_to_number([0,5]))

print("Test 3 - all same digit")
print("  expected:", 999, "| got:", list_to_number([9,9,9]))

print("Test 4 - single zero digit")
print("  expected:", 0, "| got:", list_to_number([0]))


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

grade(list_to_number)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 0, 3], expected=103)   # checks the value your code returns against this example
