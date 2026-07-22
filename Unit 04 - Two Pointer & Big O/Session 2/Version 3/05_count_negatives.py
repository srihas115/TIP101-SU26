'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 3
    Problem 5: Count Negatives

    The **sliding window technique** is an algorithmic technique often used to
    find a subarray or substring that meets certain criteria. It works by
    initializing two pointers to point at the start and end of a ‘window’ or
    subsection of the string/array at a time. The pointers are then
    incremented to slide the window and examine a different subarray or
    substring.

    Use the sliding window technique to solve the following problem:

    Write a function `count_negatives()` that takes in a list of integers
    `lst` and a positive number `k` as parameters. The function returns a list
    where each element represents the count of the number of negative values
    of each sublist of size `k` in `lst`.

    Write your solution for `count_negatives` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `count_negatives` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_negatives(k, nums):
    pass

lst = [-1, 2, -2, 3, 5, -7, -5]
print(count_negatives(lst, 3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: calls follow the same (list, k) argument order as the example call above.

print("Test 1 - k equals the length of the list (single window)")
print("  expected:", [2], "| got:", count_negatives([-1,-2,3], 3))

print("Test 2 - no negatives at all")
print("  expected:", [0,0,0], "| got:", count_negatives([1,2,3,4], 2))

print("Test 3 - all negative")
print("  expected:", [2,2], "| got:", count_negatives([-1,-2,-3], 2))


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

grade(count_negatives)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(3, [-1, 2, -2, 3, 5, -7, -5], expected=[2, 1, 1, 1, 2])   # checks the value your code returns against this example
