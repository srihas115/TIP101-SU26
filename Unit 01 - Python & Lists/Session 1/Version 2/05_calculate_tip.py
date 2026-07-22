'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 5: Calculate Tip

  Write a function `calculate_tip()` that takes in a float `bill` and a
  string `service_quality` as parameters. If `service_quality` is `"poor"`,
  the function should return 10% of the `bill` value. If `service_quality`
  is `"average"`, the function should return 15% of the `bill` value. If
  `service_quality` is `"excellent"`, the function should return 20% of the
  `bill` value. If `service_quality` is any other value, the function should
  return `None`.

  Write your solution for `calculate_tip` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `calculate_tip` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return .1 * bill
    elif service_quality == "average":
        return .15 * bill
    elif service_quality == "excellent":
        return .2 * bill
    else:
        return None

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - bill=0, poor service (zero tip)")
print("  expected:", 0.0, "| got:", calculate_tip(0, "poor"))

print("Test 2 - bill=100, excellent service")
print("  expected:", 20.0, "| got:", calculate_tip(100, "excellent"))

print("Test 3 - unrecognized service_quality string")
print("  expected:", None, "| got:", calculate_tip(50, "great"))

print("Test 4 - negative bill, poor service")
print("  expected:", -5.0, "| got:", calculate_tip(-50, "poor"))

print("Test 5 - case-sensitive mismatch ('Poor' vs 'poor')")
print("  expected:", None, "| got:", calculate_tip(50, "Poor"))

print("Test 6 - empty string service_quality")
print("  expected:", None, "| got:", calculate_tip(50, ""))


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

grade(calculate_tip)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(44.53, 'average', expected=6.6795)   # checks the value your code returns against this example
