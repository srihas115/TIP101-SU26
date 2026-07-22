'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 1: Hello User!

  Write a function `greet_user()` that takes in a string `name` as a
  parameter and prints `"Hello <name>"`.

  Write your solution for `greet_user` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `greet_user` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def greet_user(name):
    print("Hello", name)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - basic name")
print("  expected printed output: Hello Michael")
greet_user("Michael")

print("Test 2 - empty string name")
print("  expected printed output: Hello ")
greet_user("")

print("Test 3 - single character name")
print("  expected printed output: Hello X")
greet_user("X")

print("Test 4 - name with spaces")
print("  expected printed output: Hello Mary Jane")
greet_user("Mary Jane")


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

grade(greet_user)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('Michael', expected='Hello Michael')   # checks the printed output against this example
