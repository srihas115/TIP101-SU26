'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 1
  Problem 6: Calculate GPA

  Write a function `calculate_gpa()` that calculates the grade point average
  (GPA) for a student based on their course grades and returns the `gpa` as
  a float. The function takes in a dictionary `report_card` as a parameter
  where each key-value pair represents a course and the grade received in
  that course respectively. The grades are represented as strings (`"A"`,
  `"B"`, `"C"`, `"D"`, `"F"`) and each grade corresponds to a certain number
  of grade points:

  `"A"` = 4 `"B"` = 3 `"C"` = 2 `"D"` = 1 `"F"` = 0

  A GPA is calculated by finding the average of all grade points.

  Write your solution for `calculate_gpa` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `calculate_gpa` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def calculate_gpa(report_card):
    pass  # replace this line with your solution













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
