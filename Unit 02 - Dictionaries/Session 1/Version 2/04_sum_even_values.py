'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 4: Sum Even Values

  Write a function `sum_even_values()` that returns the sum of all even
  values in a given `dictionary`. Assume the dictionary values are all
  integers.

  Write your solution for `sum_even_values` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sum_even_values` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sum_even_values(dictionary):
    pass

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dictionary")
print("  expected:", 0, "| got:", sum_even_values({}))

print("Test 2 - all odd values")
print("  expected:", 0, "| got:", sum_even_values({"a": 1, "b": 3, "c": 5}))

print("Test 3 - all even values")
print("  expected:", 12, "| got:", sum_even_values({"a": 2, "b": 4, "c": 6}))

print("Test 4 - includes a zero value (0 is even)")
print("  expected:", 6, "| got:", sum_even_values({"a": 0, "b": 6, "c": 1}))

print("Test 5 - includes negative even values")
print("  expected:", -2, "| got:", sum_even_values({"a": -4, "b": 1, "c": 2}))

print("Test 6 - single key-value pair, even value")
print("  expected:", 10, "| got:", sum_even_values({"a": 10}))


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

grade(sum_even_values)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'a': 4, 'b': 1, 'c': 2, 'd': 8}, expected=14)   # checks the value your code returns against this example
