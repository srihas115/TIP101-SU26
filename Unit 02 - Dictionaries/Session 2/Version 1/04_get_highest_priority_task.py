'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 1
  Problem 4: Highest Priority Task

  Given a dictionary `tasks` where keys are task names and values are
  priorities (1-10, where 10 is the highest priority), write a function
  `get_highest_priority_task()` that removes the task with the highest
  priority from the dictionary and returns its name. If two tasks have the
  same priority, return the task that comes first in the alphabet.

  Write your solution for `get_highest_priority_task` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `get_highest_priority_task` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def get_highest_priority_task(tasks):
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

grade(get_highest_priority_task)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'task1': 8, 'task2': 10, 'task3': 9, 'task4': 10, 'task5': 7}, expected='task2')   # checks the value your code returns against this example
