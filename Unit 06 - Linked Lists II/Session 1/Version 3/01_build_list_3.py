'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 1  ·  Version 3
  Problem 1: The Power of One
  Write your solution in the space provided below, then click ▶ Run to validate it.
  (Full instructions and examples are in the problem set.)

  ⚠️  Keep every class, method, and function name exactly as the problem gives it,
      and use the exact variable names it asks for — the problem set solution validator looks those up
      by name (they're case-sensitive). If it can't find one, the results will tell
      you which name is missing.
==============================================================================
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Recreate this list in a single line of code
head = Node("Ash")
misty = Node("Misty")
brock = Node("Brock")
head.next = misty
luigi.next = brock


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import check_setup

check_setup()   # ▶ Run this file to validate your work
