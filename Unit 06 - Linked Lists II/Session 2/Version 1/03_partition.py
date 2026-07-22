class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

'''
1. understand

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

result:
1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3


create two linked lists: greater or less than the value

'''

def partition(head, val):
    smaller = None
    bigger = None
    curr = head
    
    
    pass

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# small list = 1 -> 2 -> 2
# big list = 4 -> 3 -> 5


# result: 1 -> 2 -> 2 -> 4 -> 3 -> 5 

# head = 1, val = 3

# i really want to work on this later - jessica


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

grade(partition)   # ▶ Run this file to validate your solution
