'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 3
  Problem 4: Group By Frequency

  Write a function `group_by_frequency()` that takes in a list `lst` and
  returns a dictionary where keys represent the frequency of unique elements
  within `lst` and values represent a list of elements with the same
  frequency.

  Write your solution for `group_by_frequency` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `group_by_frequency` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def group_by_frequency(lst):
    pass

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", {}, "| got:", group_by_frequency([]))

print("Test 2 - all unique elements (all frequency 1)")
print("  expected:", {1: ['a','b','c']}, "| got:", group_by_frequency(['a','b','c']))

print("Test 3 - all elements the same")
print("  expected:", {3: ['x']}, "| got:", group_by_frequency(['x','x','x']))

print("Test 4 - single-element list")
print("  expected:", {1: ['z']}, "| got:", group_by_frequency(['z']))


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

grade(group_by_frequency)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e'], expected={1: ['a', 'b'], 2: ['c', 'd'], 3: ['e']})   # checks the value your code returns against this example
