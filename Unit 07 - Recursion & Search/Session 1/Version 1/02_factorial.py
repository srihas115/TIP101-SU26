# Time: O(n) because n recursive calls before hitting the base case
# Space: O(n) because n stack frames alive simultaneously since each call is waiting on n * factorial(n-1) to return before it can multiply and return itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))
# Example Input: 5


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

grade(factorial)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, expected=120)   # checks the value your code returns against this example
