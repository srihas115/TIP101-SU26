'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 2
    Problem 12: List Occurrences

    Write a function `find_all_occurrences()` that takes in a list `lst` and a
    value `target` as parameters and returns a list of all indices where
    `target` is found in `lst`.

    Write your solution for `find_all_occurrences` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_all_occurrences` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_all_occurrences(lst, target):
    pass

lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - target not present")
print("  expected:", [], "| got:", find_all_occurrences([1,2,3], 9))

print("Test 2 - empty list")
print("  expected:", [], "| got:", find_all_occurrences([], 2))

print("Test 3 - target appears once")
print("  expected:", [2], "| got:", find_all_occurrences([5,6,2,8], 2))

print("Test 4 - target appears at every index")
print("  expected:", [0,1,2], "| got:", find_all_occurrences([7,7,7], 7))


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

grade(find_all_occurrences)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 6, 5, 2, 1, 3, 2, 2], 2, expected=[1, 4, 7, 8])   # checks the value your code returns against this example
