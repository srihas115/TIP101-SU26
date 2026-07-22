'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 2: Student Directory

  Write a function `student_directory()` that takes a list of
  `student_names` as a parameter and returns a dictionary of students, where
  each student in `student_names` is a key mapped to a unique numerical ;'
  ID.

  Write your solution for `student_directory` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `student_directory` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def student_directory(student_names):
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

grade(student_directory)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['Ada Lovelace', 'Tu Youyou', 'Mae Jemison', 'Rajeshwari Chatterjee', 'Alan Turing'], expected={'Ada Lovelace': 1, 'Tu Youyou': 2, 'Mae Jemison': 3, 'Rajeshwari Chatterjee': 4, 'Alan Turing': 5})   # checks the value your code returns against this example
