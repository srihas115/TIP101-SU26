'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 2
    Problem 6: Reverse List

    Write a function `reverse_list()` that takes in a list `lst` as a
    parameter and returns a new list containing the elements of `lst` in
    reverse order.

    Write your solution for `reverse_list` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `reverse_list` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def reverse_list(lst):
    pass

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", reverse_list([]))

print("Test 2 - single-element list")
print("  expected:", [9], "| got:", reverse_list([9]))

print("Test 3 - list with duplicate values")
print("  expected:", [2,2,1], "| got:", reverse_list([1,2,2]))

print("Test 4 - negative numbers")
print("  expected:", [-3,-2,-1], "| got:", reverse_list([-1,-2,-3]))


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

grade(reverse_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], expected=[5, 4, 3, 2, 1])   # checks the value your code returns against this example
