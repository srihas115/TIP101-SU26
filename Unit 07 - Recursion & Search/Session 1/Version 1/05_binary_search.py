# Time: O(log(n))
# Space: O(1)
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right: # We need to check that last singled out element if left == right (one last element left over in the sliced list)
        # mid = 0 # we need to make this (left + right) / 2
        mid = (left + right) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1      # we need to exclude the mid itself
        else:
            right = mid - 1     # we need to exclude the mid itself
    
    return -1 # we did not find the value

# def binary_search(lst, target):
#     pass


# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 11))

# Boundary case: two elements, target is the second one
print(binary_search([1, 3], 3))  # Expected: 1

# Boundary case: single element list
print(binary_search([5], 5))  # Expected: 0

# Target not in the list
print(binary_search([1, 3, 5, 7, 9], 4))  # Expected: -1

# Target is the first element
print(binary_search([2, 4, 6, 8, 10], 2))  # Expected: 0

# Target is the last element
print(binary_search([2, 4, 6, 8, 10], 10))  # Expected: 4


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

grade(binary_search)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 13, 15], 11, expected=5)   # checks the value your code returns against this example
