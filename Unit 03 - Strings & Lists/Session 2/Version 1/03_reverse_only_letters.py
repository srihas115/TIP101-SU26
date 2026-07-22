def reverse_only_letters(s):
    pass

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no letters (all punctuation, unchanged)")
print("  expected:", "---", "| got:", reverse_only_letters("---"))

print("Test 2 - all letters (simple full reverse)")
print("  expected:", "cba", "| got:", reverse_only_letters("abc"))

print("Test 3 - single letter")
print("  expected:", "a", "| got:", reverse_only_letters("a"))

print("Test 4 - empty string")
print("  expected:", "", "| got:", reverse_only_letters(""))


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

grade(reverse_only_letters)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('a-bC-dEf-ghIj', expected='j-Ih-gfE-dCba')   # checks the value your code returns against this example
