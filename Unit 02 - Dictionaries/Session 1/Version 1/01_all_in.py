'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 1  ·  Version 1
    Problem 1: All In

    Write a function `all_in()` that takes in a list of integers `a` and a
    list of integers `b` as parameters. Given these two lists, return `True`
    if *every* element in list `a` is in list `b`. Return `False` otherwise.

    Write your solution for `all_in` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `all_in` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def all_in(a, b):
    for x in a:
        found = False
        for y in b:
            if x == y:
                found = True
                break
        if not found:
            return False
    return True

lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list a (vacuously true)")
print("  expected:", True, "| got:", all_in([], [1, 2, 3]))

print("Test 2 - empty list b, non-empty a")
print("  expected:", False, "| got:", all_in([1], []))

print("Test 3 - both lists empty")
print("  expected:", True, "| got:", all_in([], []))

print("Test 4 - duplicates in a, all present in b")
print("  expected:", True, "| got:", all_in([1, 1, 2], [1, 2, 3]))

print("Test 5 - a has an element not in b")
print("  expected:", False, "| got:", all_in([1, 4], [1, 2, 3]))

print("Test 6 - identical lists")
print("  expected:", True, "| got:", all_in([1, 2, 3], [1, 2, 3]))


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

grade(all_in)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2], [1, 2, 3], expected=True)   # checks the value your code returns against this example
