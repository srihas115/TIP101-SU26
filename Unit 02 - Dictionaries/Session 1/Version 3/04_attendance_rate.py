def attendance_rate(attendance_list):
    pass

attendance_list = {
    "Bluey": "Present",
    "Bingo": "Absent",
    "Snickers": "Present",
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dict (no students, 0% by convention)")
print("  expected:", 0.0, "| got:", attendance_rate({}))

print("Test 2 - single key-value pair, present")
print("  expected:", 100.0, "| got:", attendance_rate({"Bluey": "Present"}))

print("Test 3 - single key-value pair, absent")
print("  expected:", 0.0, "| got:", attendance_rate({"Bluey": "Absent"}))

print("Test 4 - all present")
print("  expected:", 100.0, "| got:", attendance_rate({"A": "Present", "B": "Present"}))

print("Test 5 - all absent")
print("  expected:", 0.0, "| got:", attendance_rate({"A": "Absent", "B": "Absent"}))


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

grade(attendance_rate)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'Bluey': 'Present', 'Bingo': 'Absent', 'Snickers': 'Present', 'Winton': 'Absent'}, expected=50.0)   # checks the value your code returns against this example
