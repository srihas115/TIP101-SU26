'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 2  ·  Version 2
    Problem 2: Dictionary Intersection

    Write a function `dict_intersection()` that takes in two dictionaries as
    parameters and returns a new dictionary containing the key-value pairs
    found in both dictionaries.

    Write your solution for `dict_intersection` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `dict_intersection` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def dict_intersection(d1, d2):
    pass

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
print(dict_intersection(d1, d2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dicts")
print("  expected:", {}, "| got:", dict_intersection({}, {}))

print("Test 2 - no matching key-value pairs")
print("  expected:", {}, "| got:", dict_intersection({"a":1}, {"a":2}))

print("Test 3 - all pairs match")
print("  expected:", {"x":1,"y":2}, "| got:", dict_intersection({"x":1,"y":2}, {"x":1,"y":2}))

print("Test 4 - key present in both but with different values (excluded)")
print("  expected:", {}, "| got:", dict_intersection({"k":1}, {"k":2}))


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

grade(dict_intersection)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 4}, expected={'b': 2})   # checks the value your code returns against this example
