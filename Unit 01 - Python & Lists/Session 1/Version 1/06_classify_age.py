'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 1
  Problem 6: Classify Age

  Write a function `classify_age()` that takes an integer `age` as a
  parameter and returns `"child"` if the age is less than 18, and returns
  `"adult"` otherwise.

  Example Usage:

  Write your solution for `classify_age` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `classify_age` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - age exactly 18 (boundary, adult)")
print("  expected:", "adult", "| got:", classify_age(18))

print("Test 2 - age 17 (just under boundary, child)")
print("  expected:", "child", "| got:", classify_age(17))

print("Test 3 - age 0")
print("  expected:", "child", "| got:", classify_age(0))

print("Test 4 - negative age")
print("  expected:", "child", "| got:", classify_age(-5))

print("Test 5 - large age")
print("  expected:", "adult", "| got:", classify_age(150))


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

grade(classify_age)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(18, expected='adult')   # checks the value your code returns against this example
