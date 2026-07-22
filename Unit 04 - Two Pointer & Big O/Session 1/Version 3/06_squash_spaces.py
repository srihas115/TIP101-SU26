'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 3
  Problem 6: Squash Spaces

  The two-pointer approach can also be used with two pointers that iterate
  forward through a list or string at different rates. Use two pointers to
  solve the following problem:

  Write a function `squash_spaces()` that takes in a string `s` as a
  parameter and returns a new string with each substring with consecutive
  spaces reduced to a single space. Assume `s` can contain leading or
  trailing spaces, but in the result should be trimmed. *Do not use any of
  the built-in `trim` methods.*

  Write your solution for `squash_spaces` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `squash_spaces` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def squash_spaces(s):
    pass

print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", "", "| got:", squash_spaces(""))

print("Test 2 - only spaces")
print("  expected:", "", "| got:", squash_spaces("     "))

print("Test 3 - single word, no spaces")
print("  expected:", "word", "| got:", squash_spaces("word"))


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

grade(squash_spaces)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('  hello    world  ', expected='hello world')   # checks the value your code returns against this example
