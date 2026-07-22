'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 1
    Problem 5: Max Difference

    Write a function `max_difference()` that takes in a list of integers `lst`
    and returns the difference between the smallest and largest value in the
    list.

    Write your solution for `max_difference` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `max_difference` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def max_difference(lst):
    if len(lst) == 0 or len(lst) == 1:
        return 0
    
    min = lst[0]
    max = lst[0]
    
    for num in lst:
        if num > max:
            max = num
        if num < min:
            min = num
    
    return max - min
    

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", 20, "| got:", max_difference([5,22,8,10,2]))

print("Test 2 - single-element list (no difference)")
print("  expected:", 0, "| got:", max_difference([7]))

print("Test 3 - negative numbers")
print("  expected:", 9, "| got:", max_difference([-5,-1,-10]))

print("Test 4 - all elements equal")
print("  expected:", 0, "| got:", max_difference([4,4,4]))

print("Test 5 - already-sorted ascending list")
print("  expected:", 4, "| got:", max_difference([1,2,3,4,5]))


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

grade(max_difference)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 22, 8, 10, 2], expected=20)   # checks the value your code returns against this example
