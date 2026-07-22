# Time: O(n)
# Space: O(n)
def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)

print("Recursive")
repeat_hello(5)

# Time: O(n)
# Space: O(1)
def repeat_hello_iterative(n):
    for i in range(n):
        print("Hello")

print("Iterative")     
repeat_hello_iterative(5)


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

grade(repeat_hello_iterative)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, expected='Hello\nHello\nHello\nHello\nHello')   # checks the printed output against this example
