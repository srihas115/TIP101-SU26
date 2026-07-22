'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 3
  Problem 5: Exclusive Elements

  Write a function `exclusive_elements()` that takes in two integer lists
  `lst1` and `lst2` as parameters and returns a new list that contains the
  elements that are exclusively in one list only (*elements that are in
  `lst1` but not in `lst2` and elements that are in `lst2` but not in
  `lst1`*)

  Write your solution for `exclusive_elements` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `exclusive_elements` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def exclusive_elements(lst1, lst2):
    pass

lst1 = [3,1,8,10]
lst2 = [4,5,3,7,8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty lists")
print("  expected:", [], "| got:", exclusive_elements([], []))

print("Test 2 - identical lists (nothing exclusive)")
print("  expected:", [], "| got:", exclusive_elements([1,2], [1,2]))

print("Test 3 - completely disjoint lists")
print("  expected:", [1,2,3,4], "| got:", exclusive_elements([1,2], [3,4]))

print("Test 4 - one list empty")
print("  expected:", [5,6], "| got:", exclusive_elements([5,6], []))


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

grade(exclusive_elements)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 1, 8, 10], [4, 5, 3, 7, 8], expected=[1, 10, 4, 5, 7])   # checks the value your code returns against this example
