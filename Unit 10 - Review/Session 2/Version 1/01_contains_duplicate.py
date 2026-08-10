'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 1
    Problem 1: Contains Duplicates

    Given an integer array `nums`, return `True` if any value appears **at
    least twice** in the array, and return `False` if every element is
    distinct.

    Write your solution for `contains_duplicate` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `contains_duplicate` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 
    input: list of ints
    output: boolean - True if any value appears more than once, False otherwise
    core logic: using a set to determine if a number is seen
    
Match:
    seen set
    
Plan:
    initialize a set
    loop through nums
        if the number in seen set?
            return true
        add num to set
    return false
'''


def contains_duplicate(nums):
    pass  # replace this line with your solution












    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
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

grade(contains_duplicate)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 1], expected=True)   # checks the value your code returns against this example
