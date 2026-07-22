'''
==============================================================================
    Unit 10: Review  ·  Session 1  ·  Version 3
    Problem 3: Delete N Nodes after M Nodes

    You are given the `head` of a linked list and two integers `m` and `n`.

    Traverse the linked list and remove some nodes in the following way:

    - Start with the head as the current node. - Keep the first `m` nodes
    starting with the current node. - Remove the next `n` nodes - Keep
    repeating steps 2 and 3 until you reach the end of the list.

    Return *the head of the modified list after removing the mentioned nodes*.

    Write your solution for `delete_nodes` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `delete_nodes` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

def delete_nodes(head, m, n):
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
from problem_set_solution_validator import grade, test

grade(delete_nodes)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 2, 3, expected=[1, 2, 6, 7, 11, 12])   # checks the value your code returns against this example
