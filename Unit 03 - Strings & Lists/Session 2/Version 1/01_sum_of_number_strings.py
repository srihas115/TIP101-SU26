'''
==============================================================================
    Unit 3: Strings & Lists  ·  Session 2  ·  Version 1
    Problem 1: Sum of Strings

    Write a function `sum_of_number_strings()` that takes in a list of strings
    `nums`. Each string is a representations of integers. The function should
    return the sum of these strings as an integer.

    Write your solution for `sum_of_number_strings` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `sum_of_number_strings` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sum_of_number_strings(nums):
    pass

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", sum_of_number_strings([]))

print("Test 2 - single-element list")
print("  expected:", 7, "| got:", sum_of_number_strings(["7"]))

print("Test 3 - negative number strings")
print("  expected:", 5, "| got:", sum_of_number_strings(["-5", "10"]))

print("Test 4 - list containing a zero string")
print("  expected:", 10, "| got:", sum_of_number_strings(["0", "10"]))


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

grade(sum_of_number_strings)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['10', '20', '30'], expected=60)   # checks the value your code returns against this example
