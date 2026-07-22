def is_monotonic(nums):
    if len(nums) == 0:
        return True
    increasing = True
    decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            increasing = False
        if nums[i] < nums[i - 1]:
            decreasing = False
    
    return increasing or decreasing

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (vacuously monotonic)")
print("  expected:", True, "| got:", is_monotonic([]))

print("Test 2 - single element list")
print("  expected:", True, "| got:", is_monotonic([5]))

print("Test 3 - all equal elements")
print("  expected:", True, "| got:", is_monotonic([4, 4, 4, 4]))

print("Test 4 - strictly increasing")
print("  expected:", True, "| got:", is_monotonic([1, 2, 3, 4]))

print("Test 5 - strictly decreasing")
print("  expected:", True, "| got:", is_monotonic([9, 7, 5, 1]))

print("Test 6 - non-monotonic with a dip then rise")
print("  expected:", False, "| got:", is_monotonic([1, 5, 2, 8]))


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

grade(is_monotonic)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 2, 3, 10], expected=True)   # checks the value your code returns against this example
