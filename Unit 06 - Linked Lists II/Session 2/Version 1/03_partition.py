'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 2  ·  Version 1
    Problem 3: Partition List Around Value

    Given the `head` of a linked list and a value `val`, partition a linked
    list around `val` such that all nodes with values less than `val` come
    before nodes with values greater than or equal to `val`.

    Write your solution for `partition` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `partition` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic):
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
result:
1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3

Match:

Plan:
create two linked lists: greater or less than the value

'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

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
