'''
==============================================================================
    Unit 3: Strings & Lists  ·  Session 2  ·  Version 1
    Problem 2: Remove Duplicates

    Write a function `remove_duplicates()` that takes in a *sorted* list of
    integers `nums` as a parameter and removes all duplicates in the list. The
    function returns the modified list.

    Write your solution for `remove_duplicates` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `remove_duplicates` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def remove_duplicates(nums):
    pass

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [1,2,3,4,5,6], "| got:", remove_duplicates([1,1,1,2,3,4,4,5,6,6]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", remove_duplicates([]))

print("Test 3 - single-element list")
print("  expected:", [9], "| got:", remove_duplicates([9]))

print("Test 4 - no duplicates (already unique)")
print("  expected:", [1,2,3], "| got:", remove_duplicates([1,2,3]))

print("Test 5 - all elements the same")
print("  expected:", [4], "| got:", remove_duplicates([4,4,4,4]))


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

grade(remove_duplicates)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 1, 1, 2, 3, 4, 4, 5, 6, 6], expected=[1, 2, 3, 4, 5, 6])   # checks the value your code returns against this example
