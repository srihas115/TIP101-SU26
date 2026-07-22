'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 2
  Problem 1: String to Integer

  Write a function `string_to_integer_mapping()` that takes in a string of
  digits `s` as a parameter and returns a list where each element is the
  integer value of the corresponding digit in the string.

  Write your solution for `string_to_integer_mapping` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `string_to_integer_mapping` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def string_to_integer_mapping(s):
    pass

s = "12345"
print(string_to_integer_mapping(s))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", [], "| got:", string_to_integer_mapping(""))

print("Test 2 - single digit")
print("  expected:", [7], "| got:", string_to_integer_mapping("7"))

print("Test 3 - all same digit")
print("  expected:", [0,0,0], "| got:", string_to_integer_mapping("000"))


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

grade(string_to_integer_mapping)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('12345', expected=[1, 2, 3, 4, 5])   # checks the value your code returns against this example
