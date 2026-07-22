'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 1
  Problem 5: Find Majority Element

  Write a function `find_majority_element()` that takes in a list of
  integers `elements` and finds the majority element in the list. A majority
  element is an element that appears more than `n/2` times where `n` is the
  size of the list. If there is no majority element, return `None`.

  Write your solution for `find_majority_element` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_majority_element` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_majority_element(elements):
    pass

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no majority element")
print("  expected:", None, "| got:", find_majority_element([1,2,3]))

print("Test 2 - single-element list (trivially a majority)")
print("  expected:", 9, "| got:", find_majority_element([9]))

print("Test 3 - two identical elements (majority)")
print("  expected:", 4, "| got:", find_majority_element([4,4]))

print("Test 4 - two different elements (no majority)")
print("  expected:", None, "| got:", find_majority_element([4,5]))


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

grade(find_majority_element)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 2, 1, 1, 1, 2, 2], expected=2)   # checks the value your code returns against this example
