# UPI
# Understand: make two nodes and assign values to them 
# Plan: create node objects
# Implement: (below)
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

# --- Merged from Problem 10: Linking Nodes.py ---
# UPI
# Understand: connect two nodes
# Plan: use .next method 
# Implement: (below)
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
'''
        
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
