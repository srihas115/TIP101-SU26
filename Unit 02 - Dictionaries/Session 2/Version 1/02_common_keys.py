'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 1
  Problem 2: Keys in Common

  Write a function that takes in two dictionaries, `dict1` and `dict2` and
  finds all keys common to both dictionaries. The function returns a list of
  common keys.

  Write your solution for `common_keys` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `common_keys` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def common_keys(dict1, dict2):
    pass

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dicts")
print("  expected:", [], "| got:", common_keys({}, {}))

print("Test 2 - no common keys")
print("  expected:", [], "| got:", common_keys({"a":1}, {"b":2}))

print("Test 3 - all keys common")
print("  expected:", ["x","y"], "| got:", common_keys({"x":1,"y":2}, {"x":9,"y":9}))

print("Test 4 - one dict is empty")
print("  expected:", [], "| got:", common_keys({"a":1}, {}))


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

grade(common_keys)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'c': 5, 'd': 6}, expected=['b', 'c'])   # checks the value your code returns against this example
