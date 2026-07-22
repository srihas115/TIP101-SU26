def reverse_list(lst):
    pass

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", reverse_list([]))

print("Test 2 - single-element list")
print("  expected:", [9], "| got:", reverse_list([9]))

print("Test 3 - two-element list")
print("  expected:", [2, 1], "| got:", reverse_list([1, 2]))

print("Test 4 - already palindromic list (unchanged)")
print("  expected:", [1, 2, 1], "| got:", reverse_list([1, 2, 1]))

print("Test 5 - all-duplicate elements")
print("  expected:", [5, 5, 5], "| got:", reverse_list([5, 5, 5]))


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

grade(reverse_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], expected=[5, 4, 3, 2, 1])   # checks the value your code returns against this example
