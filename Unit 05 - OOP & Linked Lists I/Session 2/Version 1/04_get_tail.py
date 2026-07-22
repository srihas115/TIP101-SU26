'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
    Problem 4: Get Tail

    Write a function `get_tail()` that takes in the `head` of a linked list as
    a parameter.

    Return the value of the `tail`. If the list is empty, return `None`.

    *Note: The "tail" of a list is the last element in the linked list.
    Equivalent to `lst[-1]` in a normal list.*

    Write your solution for `get_tail` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `get_tail` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_tail(head):
    if head is None:
        return None
    
    curr = head
    while curr.next is not None:
        curr = curr.next

    return curr.value

# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3


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

grade(get_tail)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=3)   # checks the value your code returns against this example
