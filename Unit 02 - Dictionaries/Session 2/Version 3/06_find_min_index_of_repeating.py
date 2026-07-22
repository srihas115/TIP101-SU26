def find_min_index_of_repeating(nums):
    pass

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", None, "| got:", find_min_index_of_repeating([]))

print("Test 2 - single-element list")
print("  expected:", None, "| got:", find_min_index_of_repeating([7]))

print("Test 3 - duplicate at the very start")
print("  expected:", 0, "| got:", find_min_index_of_repeating([1,1,2,3]))

print("Test 4 - all unique elements")
print("  expected:", None, "| got:", find_min_index_of_repeating([1,2,3,4]))


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

grade(find_min_index_of_repeating)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 3, 4, 3, 6, 4], expected=1)   # checks the value your code returns against this example
