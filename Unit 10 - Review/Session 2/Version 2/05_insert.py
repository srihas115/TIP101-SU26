'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 2
    Problem 5: Insert into Sorted Circular Linked List

    Given a linked list node `start_node` that is a node in a circularly
    linked list sorted in non-descending order, write a function `insert()`
    that inserts a value `insert_val` into the list such that it remains a
    sorted circular list. The given node can be a reference to any single node
    in the list and may not necessarily be the smallest value in the circular
    list.

    If there are multiple suitable places for insertion, you may choose any
    place to insert the new value. After the insertion, the circular list
    should remain sorted.

    If the list is empty (i.e., the given node is `null`), you should create a
    new single circular list and return the reference to that single node.
    Otherwise, you should return the originally given node.

    Write your solution for `insert` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `insert` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert(start_node, insert_val):
    pass


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

grade(insert)   # ▶ Run this file to validate your solution
