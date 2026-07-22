def longest_common_prefix(strings):
    pass

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list of strings")
print("  expected:", "", "| got:", longest_common_prefix([]))

print("Test 2 - single string in the list")
print("  expected:", "hello", "| got:", longest_common_prefix(["hello"]))

print("Test 3 - all strings identical")
print("  expected:", "abc", "| got:", longest_common_prefix(["abc", "abc"]))

print("Test 4 - no common prefix at all")
print("  expected:", "", "| got:", longest_common_prefix(["dog", "racecar", "car"]))

print("Test 5 - one string is a prefix of the others")
print("  expected:", "ab", "| got:", longest_common_prefix(["ab", "abc", "abcd"]))


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

grade(longest_common_prefix)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['flower', 'flow', 'flight'], expected='fl')   # checks the value your code returns against this example
