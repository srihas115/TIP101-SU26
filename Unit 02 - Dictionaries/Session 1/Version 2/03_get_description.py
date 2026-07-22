def get_description(info, keys):
    for key in keys:
        print(info[key])

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: get_description() prints instead of returning, so we describe expected printed output.
# Also note: this problem's provided starter code has a bug (uses info[key], which raises a
# KeyError for a missing key instead of printing None). Until the bug is fixed, these calls
# involving a missing key will raise a KeyError instead of printing "None".

print("Test 1 - all requested keys are present")
print("  expected printed output: Tom then 30")
get_description({"name": "Tom", "age": 30}, ["name", "age"])

print("Test 2 - empty keys list (should print nothing)")
print("  expected printed output: (nothing printed)")
get_description({"name": "Tom"}, [])

print("Test 3 - empty info dictionary with a missing key")
print("  expected printed output: None (once bug is fixed); currently raises KeyError")
try:
    get_description({}, ["missing"])
except KeyError:
    print("  KeyError raised (bug not yet fixed)")

print("Test 4 - same key requested multiple times")
print("  expected printed output: engineer then engineer")
get_description({"occupation": "engineer"}, ["occupation", "occupation"])


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

grade(get_description)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'name': 'Tom', 'age': '30', 'occupation': 'engineer'}, ['name', 'occupation', 'salary'], expected='Tom\nengineer\nNone')   # checks the printed output against this example
