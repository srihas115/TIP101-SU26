'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 2  ·  Version 1
  Problem 7: Evens List

  Write a function `get_evens()` that takes in a list of integers `lst` as a
  parameter and returns a list of all even numbers in the list.

  Write your solution for `get_evens` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `get_evens` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def get_evens(lst):
    evens_lst = []
    for num in lst:
        if num % 2 == 0:
            evens_lst.append(num)
    return evens_lst

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [2, 4], "| got:", get_evens([1,2,3,4]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", get_evens([]))

print("Test 3 - all odd numbers")
print("  expected:", [], "| got:", get_evens([1,3,5]))

print("Test 4 - negative even numbers")
print("  expected:", [-2, -4], "| got:", get_evens([-2,-3,-4]))

print("Test 5 - list containing zero (zero is even)")
print("  expected:", [0], "| got:", get_evens([0, 1]))


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

grade(get_evens)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=[2, 4])   # checks the value your code returns against this example
