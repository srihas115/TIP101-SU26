'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 2  ·  Version 1
  Problem 12: Linear Search

  Write a function `linear_search()` that takes in a list `lst` and value
  `target` as parameters. The function returns the index of `target` in
  `lst` if found. If `target` is not found in `lst`, return `-1`.

  Write your solution for `linear_search` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `linear_search` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)

lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - target found (matches example)")
print("  expected:", 2, "| got:", linear_search([1,4,5,2,8], 5))

print("Test 2 - target not found")
print("  expected:", -1, "| got:", linear_search([1,4,5,2,8], 10))

print("Test 3 - empty list")
print("  expected:", -1, "| got:", linear_search([], 3))

print("Test 4 - single-element list, target present")
print("  expected:", 0, "| got:", linear_search([9], 9))

print("Test 5 - duplicate values, returns first occurrence")
print("  expected:", 1, "| got:", linear_search([5,3,3,3], 3))

print("Test 6 - target at last index")
print("  expected:", 3, "| got:", linear_search([1,2,3,4], 4))


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

grade(linear_search)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 4, 5, 2, 8], 5, expected=2)   # checks the value your code returns against this example
