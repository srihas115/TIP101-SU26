'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 3
  Problem 5: No Duplicates Allowed

  Write a function that takes in a list of integers `nums` as a parameter
  and removes all duplicates. The function should return a list containing
  the unique elements in the order of their **last** occurrence in the
  original list.

  Write your solution for `remove_duplicates_from_front` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `remove_duplicates_from_front` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def remove_duplicates_from_front(nums):
    pass

nums = [6,5,3,5,2,8,3]
print(remove_duplicates_from_front(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", remove_duplicates_from_front([]))

print("Test 2 - no duplicates (order unchanged)")
print("  expected:", [1,2,3], "| got:", remove_duplicates_from_front([1,2,3]))

print("Test 3 - all elements the same")
print("  expected:", [5], "| got:", remove_duplicates_from_front([5,5,5]))

print("Test 4 - single-element list")
print("  expected:", [9], "| got:", remove_duplicates_from_front([9]))


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

grade(remove_duplicates_from_front)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([6, 5, 3, 5, 2, 8, 3], expected=[6, 5, 2, 8, 3])   # checks the value your code returns against this example
