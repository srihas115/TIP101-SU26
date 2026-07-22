def sort_array_by_parity(nums):
    pass

nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: any ordering where odd values land on odd indices and even values land on
# even indices is valid, so these tests check that *property* rather than one exact list.

def _is_valid_parity_arrangement(original, result):
    if sorted(result) != sorted(original):
        return False
    for i, val in enumerate(result):
        if val % 2 != i % 2:
            return False
    return True

print("Test 1 - matches example [4,2,5,7]")
original1 = [4,2,5,7]
result1 = sort_array_by_parity(original1)
print("  expected:", True, "| got:", _is_valid_parity_arrangement(original1, result1))

print("Test 2 - two-element list [2,3]")
original2 = [2,3]
result2 = sort_array_by_parity(original2)
print("  expected:", True, "| got:", _is_valid_parity_arrangement(original2, result2))

print("Test 3 - larger list")
original3 = [8,1,4,3,6,5]
result3 = sort_array_by_parity(original3)
print("  expected:", True, "| got:", _is_valid_parity_arrangement(original3, result3))


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade

grade(sort_array_by_parity)   # ▶ Run this file to validate your solution
