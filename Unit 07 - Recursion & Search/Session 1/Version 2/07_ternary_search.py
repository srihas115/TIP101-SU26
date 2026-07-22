'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 2
    Problem 7: Ternary Search

    Ternary search is a search algorithm that, similar to binary search, works
    on a sorted array. However, instead of dividing the search interval into
    two halves (as in binary search), ternary search divides it into three
    parts, using two midpoints. This reduces the problem size to approximately
    one-third in each step, rather than one-half.

    Given the pseudocode for `ternary_search()` below, implement the function.
    Evaluate the time and space complexity of your solution

    Write your solution for `ternary_search` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `ternary_search` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def ternary_search(lst, target):
    pass
    # Divide the array into three parts using two mid points (mid1 and mid2).

    # While the lower bound is less than or equal to the upper bound:
        # Compare the target value with the values at mid1 and mid2:
            # If the target value matches mid1 or mid2
                # the search is successful.
            # If the target is less than the value at mid1
                # search between the lower bound and mid1 - 1.
            # If the target is between mid1 and mid2
                # search between mid1 + 1 and mid2 - 1.
            # If the target is greater than the value at mid2
                # search between mid2 + 1 and the upper bound.
    # Return -1, indicating the target is not in the array.

# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11


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

grade(ternary_search)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 13, 15], 11, expected=5)   # checks the value your code returns against this example
