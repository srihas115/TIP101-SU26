class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

print(head.value)
print(head.next.value)
print(tail.value)
print(tail.next)

# --- Merged from Problem 10: Middle Node.py ---
print(head.next.value)
print(middle.next.value)
print(tail.next)


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
