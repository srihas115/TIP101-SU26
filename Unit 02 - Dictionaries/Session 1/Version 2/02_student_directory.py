def student_directory(student_names):
    res = {}
    
    for i in range(len(student_names)):
        res[student_names[i]] = i + 1
    
    return res

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - example from spec")
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print("  expected:", {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}, "| got:", student_directory(student_names))

print("Test 2 - empty list of student names")
print("  expected:", {}, "| got:", student_directory([]))

print("Test 3 - single student")
print("  expected:", {"Grace Hopper": 1}, "| got:", student_directory(["Grace Hopper"]))

print("Test 4 - duplicate student name (later occurrence overwrites the ID for that key)")
print("  expected:", {"Ada": 3, "Bo": 2}, "| got:", student_directory(["Ada", "Bo", "Ada"]))


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

grade(student_directory)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['Ada Lovelace', 'Tu Youyou', 'Mae Jemison', 'Rajeshwari Chatterjee', 'Alan Turing'], expected={'Ada Lovelace': 1, 'Tu Youyou': 2, 'Mae Jemison': 3, 'Rajeshwari Chatterjee': 4, 'Alan Turing': 5})   # checks the value your code returns against this example
