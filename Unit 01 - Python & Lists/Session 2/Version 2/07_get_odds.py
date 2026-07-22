def get_odds(nums):
    pass

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", get_odds([]))

print("Test 2 - all even numbers")
print("  expected:", [], "| got:", get_odds([2,4,6]))

print("Test 3 - negative odd numbers")
print("  expected:", [-1,-3], "| got:", get_odds([-1,-2,-3]))

print("Test 4 - list containing zero (zero is even, excluded)")
print("  expected:", [1], "| got:", get_odds([0,1]))


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

grade(get_odds)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 5, 1, 8, 6, 5], expected=[5, 1, 5])   # checks the value your code returns against this example
