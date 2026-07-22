'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 2  ·  Version 1
    Problem 3: Frequency Count

    Write a function that takes in a list of integers `nums` and counts the
    number of occurrences of each integer. The function returns the result as
    a dictionary with integers as keys and their counts as values.

    Write your solution for `count_occurrences` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `count_occurrences` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_occurrences(nums):
    pass

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", {1:1,2:2,3:3,4:1}, "| got:", count_occurrences([1,2,2,3,3,3,4]))

print("Test 2 - empty list")
print("  expected:", {}, "| got:", count_occurrences([]))

print("Test 3 - single-element list")
print("  expected:", {5:1}, "| got:", count_occurrences([5]))

print("Test 4 - negative numbers")
print("  expected:", {-1:2,-2:1}, "| got:", count_occurrences([-1,-1,-2]))

print("Test 5 - all same value")
print("  expected:", {7:4}, "| got:", count_occurrences([7,7,7,7]))


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

grade(count_occurrences)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 2, 3, 3, 3, 4], expected={1: 1, 2: 2, 3: 3, 4: 1})   # checks the value your code returns against this example
