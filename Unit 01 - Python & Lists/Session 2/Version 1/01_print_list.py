'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 1
    Problem 1: Print List

    Write a function `print_list()` that takes in a list `lst` as a parameter
    and prints out each item in the list.

    Write your solution for `print_list` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `print_list` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def print_list(lst):
    for item in lst:
        print(item)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_list([])

print("Test 2 - single-element list")
print("  expected printed output: pikachu")
print_list(["pikachu"])

print("Test 3 - list preserves order")
print("  expected printed output: a / b / c")
print_list(["a", "b", "c"])

print("Test 4 - list with duplicate elements")
print("  expected printed output: x / x / y")
print_list(["x", "x", "y"])


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

grade(print_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['squirtle', 'gengar', 'charizard', 'pikachu'], expected='squirtle\ngengar\ncharizard\npikachu')   # checks the printed output against this example
