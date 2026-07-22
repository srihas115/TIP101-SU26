def calculate_gpa(report_card):
    gpa = 0.0
    
    for k, v in report_card.items():
        if v == "A":
            gpa += 4.0
        elif v == "B":
            gpa += 3.0
        elif v == "C":
            gpa += 2.0
        elif v == "D":
            gpa += 1.0
        else:
            gpa += 0.0
            
    if gpa == 0.0 or len(report_card.keys()) == 0:
        return 0.0
    
    gpa /= len(report_card.keys())
    return gpa

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single course, grade A")
print("  expected:", 4.0, "| got:", calculate_gpa({"Math": "A"}))

print("Test 2 - all F grades")
print("  expected:", 0.0, "| got:", calculate_gpa({"Math": "F", "Science": "F"}))

print("Test 3 - one of each grade letter (A,B,C,D)")
print("  expected:", 2.5, "| got:", calculate_gpa({"Math": "A", "Science": "B", "History": "C", "Art": "D"}))

print("Test 4 - all grades equal (B, B)")
print("  expected:", 3.0, "| got:", calculate_gpa({"Math": "B", "Science": "B"}))

print("Test 5 - empty report card (edge case: no courses, would divide by zero)")
print("  expected printed output: 0.0, or a ZeroDivisionError depending on how the empty case is handled")
try:
    print("  got:", calculate_gpa({}))
except ZeroDivisionError:
    print("  got: ZeroDivisionError raised")


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

grade(calculate_gpa)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'Math': 'A', 'Science': 'C', 'History': 'A', 'Art': 'B', 'English': 'B', 'Spanish': 'A'}, expected=3.3333333333333335)   # checks the value your code returns against this example
