'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 1  ·  Version 3
    Problem 1: Mountain Peak

    A mountain list is defined as a list that has at least three elements,
    where there exists some `i` with `0 < i < len(lst)-1` such that `lst[0] <
    lst[1] < ... lst[i-1] < lst[i]` and `lst[i] > lst[i+1] > ... >
    lst[len(lst)-1]`.

    Given such a mountain list `lst` as a parameter, write a function that
    finds and returns the highest peak (the index `i` of the maximum element).

    Write your solution for `peak_index_in_mountain_list` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `peak_index_in_mountain_list` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def peak_index_in_mountain_list(lst):
    pass

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - minimal 3-element mountain")
print("  expected:", 1, "| got:", peak_index_in_mountain_list([1,3,1]))

print("Test 2 - peak near the start")
print("  expected:", 1, "| got:", peak_index_in_mountain_list([1,10,2,1]))

print("Test 3 - peak near the end")
print("  expected:", 3, "| got:", peak_index_in_mountain_list([1,2,3,10,5]))

print("Test 4 - negative numbers")
print("  expected:", 2, "| got:", peak_index_in_mountain_list([-5,-1,0,-2,-10]))


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

grade(peak_index_in_mountain_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([0, 3, 8, 0], expected=2)   # checks the value your code returns against this example
