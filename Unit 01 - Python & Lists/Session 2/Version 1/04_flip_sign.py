def flip_sign(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * -1
    return lst

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [-1, 2, 3, -4], "| got:", flip_sign([1,-2,-3,4]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", flip_sign([]))

print("Test 3 - all positive numbers")
print("  expected:", [-1,-2,-3], "| got:", flip_sign([1,2,3]))

print("Test 4 - all negative numbers")
print("  expected:", [1,2,3], "| got:", flip_sign([-1,-2,-3]))

print("Test 5 - list containing zero (sign flip has no effect on zero)")
print("  expected:", [0, -5], "| got:", flip_sign([0, 5]))


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

grade(flip_sign)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, -2, -3, 4], expected=[-1, 2, 3, -4])   # checks the value your code returns against this example
