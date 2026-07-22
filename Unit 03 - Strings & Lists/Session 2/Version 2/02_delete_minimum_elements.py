def delete_minimum_elements(nums):
    pass

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", delete_minimum_elements([]))

print("Test 2 - single-element list")
print("  expected:", [9], "| got:", delete_minimum_elements([9]))

print("Test 3 - already sorted ascending")
print("  expected:", [1,2,3], "| got:", delete_minimum_elements([1,2,3]))

print("Test 4 - all elements the same")
print("  expected:", [4,4,4], "| got:", delete_minimum_elements([4,4,4]))

print("Test 5 - negative numbers")
print("  expected:", [-5,-2,0], "| got:", delete_minimum_elements([0,-2,-5]))


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

grade(delete_minimum_elements)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 3, 2, 8, 3, 1], expected=[1, 2, 3, 3, 5, 8])   # checks the value your code returns against this example
