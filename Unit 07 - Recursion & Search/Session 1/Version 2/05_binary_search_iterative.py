'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 2
    Problem 5: Binary Search II

    Binary search is a searching algorithm that allows us to efficiently find
    the index of a given value within a sorted list. Given the recursive
    solution for binary search below, implement an _iterative_ (non-recursive)
    implementation of binary search.

    Evaluate the time and space complexity of your implementation.

    Write your solution for `binary_search_iterative` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `binary_search_iterative` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found within bounds

        # find middle index of list
    mid = (left + right) // 2

    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # If the target is greater than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_iterative(arr, target):
    pass

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

grade(binary_search_iterative)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 13, 15], 11, expected=5)   # checks the value your code returns against this example
