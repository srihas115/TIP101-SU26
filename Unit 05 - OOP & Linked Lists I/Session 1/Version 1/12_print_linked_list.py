class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next= next

def print_linked_list(head):
    curr = head
    while curr is not None:
        if curr.next is not None:
            print(curr.value, end=" -> ")
        else:
            print(curr.value)
        curr = curr.next
            

# input linked list: a->b->c->d->e

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
a.next = b
b.next = c
c.next = d
d.next = e

print_linked_list(a)


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

grade(print_linked_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], expected='1 -> 2 -> 3 -> 4 -> 5')   # checks the printed output against this example
