def create_dictionary(keys, values):
    res = {}
    for i in range(len(keys)):
        res[keys[i]] = values[i]
    return res
        

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty keys and values")
print("  expected:", {}, "| got:", create_dictionary([], []))

print("Test 2 - single key-value pair")
print("  expected:", {'a': 1}, "| got:", create_dictionary(['a'], [1]))

print("Test 3 - duplicate keys, later value overwrites earlier")
print("  expected:", {'a': 2}, "| got:", create_dictionary(['a', 'a'], [1, 2]))

print("Test 4 - duplicate values across distinct keys")
print("  expected:", {'a': 1, 'b': 1, 'c': 1}, "| got:", create_dictionary(['a', 'b', 'c'], [1, 1, 1]))

print("Test 5 - integer keys and values")
print("  expected:", {1: 10, 2: 20, 3: 30}, "| got:", create_dictionary([1, 2, 3], [10, 20, 30]))


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

grade(create_dictionary)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['peanut', 'dragon', 'star', 'pop', 'space'], ['butter', 'fly', 'fish', 'corn', 'ship'], expected={'peanut': 'butter', 'dragon': 'fly', 'star': 'fish', 'pop': 'corn', 'space': 'ship'})   # checks the value your code returns against this example
