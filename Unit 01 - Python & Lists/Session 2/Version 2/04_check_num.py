'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 2
    Problem 4: Check for Number

    Write a function `check_num()` that takes in a list of integers `lst` and
    an integer `num` as parameters and returns `True` if `num` is a value in
    `lst` and `False` otherwise.

    Write your solution for `check_num` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `check_num` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def check_num(lst, num):
    pass

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", False, "| got:", check_num([], 5))

print("Test 2 - num present at first index")
print("  expected:", True, "| got:", check_num([5,2,3], 5))

print("Test 3 - num present at last index")
print("  expected:", True, "| got:", check_num([5,2,3], 3))

print("Test 4 - negative number present")
print("  expected:", True, "| got:", check_num([-5,-2,3], -5))


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

grade(check_num)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 2, 3, 9, 10], 9, expected=True)   # checks the value your code returns against this example
