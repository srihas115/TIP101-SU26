class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_node(head, val):
    pass

# Example 1:
# Build: 1 -> 2 -> 3 -> (back to 1)
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
head = num1

head = delete_node(head, 2)
# Result Linked List (by values): 1 -> 3 -> 1


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade

grade(delete_node)   # ▶ Run this file to validate your solution
