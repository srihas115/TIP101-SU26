'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 1
    Problem 6: Below Threshold

    Write a function `count_less_than()` that takes in a list of integers
    `numbers` and an integer `threshold` as parameters and returns the number
    of items in `numbers` that are less than `threshold`.

    Write your solution for `count_less_than` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `count_less_than` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_less_than(numbers, threshold):
    counter = 0
    for num in numbers:
        if num < threshold:
            counter += 1
    return counter

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", 3, "| got:", count_less_than([12,8,2,4,4,10], 5))

print("Test 2 - empty list")
print("  expected:", 0, "| got:", count_less_than([], 5))

print("Test 3 - negative threshold")
print("  expected:", 2, "| got:", count_less_than([-5,-1,0,3], -1))

print("Test 4 - all elements equal to threshold (excluded, not strictly less)")
print("  expected:", 0, "| got:", count_less_than([5,5,5], 5))

print("Test 5 - all elements less than threshold")
print("  expected:", 3, "| got:", count_less_than([1,2,3], 10))


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

grade(count_less_than)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([12, 8, 2, 4, 4, 10], 5, expected=3)   # checks the value your code returns against this example
