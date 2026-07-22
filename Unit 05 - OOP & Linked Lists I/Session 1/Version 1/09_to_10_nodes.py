'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 1
  Problem 9: Node Class / Linking Nodes
  Write your solution in the space provided below, then click ▶ Run to validate it.
  (Full instructions and examples are in the problem set.)

  ⚠️  Keep every class, method, and function name exactly as the problem gives it,
      and use the exact variable names it asks for — the problem set solution validator looks those up
      by name (they're case-sensitive). If it can't find one, the results will tell
      you which name is missing.
==============================================================================
Understand (input, output, core logic):
Problem 9: make two nodes and assign values to them
Problem 10: connect two nodes

Match:

Plan:
Problem 9: create node objects
Problem 10: use .next method
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_one = Node("a")
node_two = Node("b")

print(node_one.value)
print(node_one.next)
print(node_two.value)
print(node_two.next)
        
node_one = Node("a")
node_two = Node("b")
node_one.next = node_two

print(node_one.value)
print(node_one.next.value)
print(node_two.value)


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
