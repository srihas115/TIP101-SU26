def find_poisoned_duration(time_series, duration):
    pass

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty time_series")
print("  expected:", 0, "| got:", find_poisoned_duration([], 3))

print("Test 2 - single attack")
print("  expected:", 3, "| got:", find_poisoned_duration([5], 3))

print("Test 3 - non-overlapping attacks (no reset needed)")
print("  expected:", 6, "| got:", find_poisoned_duration([1, 10], 3))

print("Test 4 - overlapping attacks, matches the walkthrough in the spec")
print("  expected:", 5, "| got:", find_poisoned_duration([1, 4], 3))


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

grade(find_poisoned_duration)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 4, 9], 3, expected=8)   # checks the value your code returns against this example
