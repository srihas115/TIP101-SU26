'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 1
  Problem 7: Make Pairs

  Write a function `divide_list()` that takes in an integer list `nums`
  consisting of `2*n` integers as parameters. The function divides `nums`
  into `n` pairs such that: - Each element belongs to exactly one pair - The
  elements present in a pair are equal

  Return `True` if `nums` can be divided into `n` pairs, otherwise return
  `False`.

  Write your solution for `divide_list` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `divide_list` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def divide_list(nums):
    pass

nums = [3,2,3,2,2,2]
print(divide_list(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - cannot be divided into pairs")
print("  expected:", False, "| got:", divide_list([1,2,3,4]))

print("Test 2 - empty list (trivially 0 pairs)")
print("  expected:", True, "| got:", divide_list([]))

print("Test 3 - all same value")
print("  expected:", True, "| got:", divide_list([5,5,5,5]))

print("Test 4 - one value has an odd count")
print("  expected:", False, "| got:", divide_list([1,1,1,2,2,2]))


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

grade(divide_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 2, 3, 2, 2, 2], expected=True)   # checks the value your code returns against this example
