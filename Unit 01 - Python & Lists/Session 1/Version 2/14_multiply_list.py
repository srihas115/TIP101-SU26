def multiply_list(lst, multiplier):
    for i in range(len(lst)):
        lst[i] = lst[i] * multiplier
    return lst

lst = [1,2,3]
new_lst = multiply_list(lst, 3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [3,6,9], "| got:", multiply_list([1,2,3], 3))

print("Test 2 - empty list")
print("  expected:", [], "| got:", multiply_list([], 5))

print("Test 3 - multiplier is 0")
print("  expected:", [0,0,0], "| got:", multiply_list([1,2,3], 0))

print("Test 4 - negative multiplier")
print("  expected:", [-3,-6,-9], "| got:", multiply_list([1,2,3], -3))

print("Test 5 - negative numbers in list")
print("  expected:", [-2,-4], "| got:", multiply_list([-1,-2], 2))


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

grade(multiply_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], 3, expected=[3, 6, 9])   # checks the value your code returns against this example
