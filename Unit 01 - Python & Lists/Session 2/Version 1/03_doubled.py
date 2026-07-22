def doubled(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * 2
    return lst

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [2,4,6], "| got:", doubled([1,2,3]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", doubled([]))

print("Test 3 - negative numbers")
print("  expected:", [-2,-4], "| got:", doubled([-1,-2]))

print("Test 4 - single-element list")
print("  expected:", [10], "| got:", doubled([5]))

print("Test 5 - list with zero")
print("  expected:", [0], "| got:", doubled([0]))


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

grade(doubled)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=[2, 4, 6])   # checks the value your code returns against this example
