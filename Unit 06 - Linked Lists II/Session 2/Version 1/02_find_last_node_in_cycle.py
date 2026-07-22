'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 1
  Problem 2: Find Last Node in a Cycle

  Given the head of a singly linked list, write a function that returns the
  last node in the cycle. If there is no cycle in the linked list, return
  None.

  Write your solution for `find_last_node_in_cycle` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_last_node_in_cycle` and its parameters exactly as given —
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


def find_last_node_in_cycle(head):
    seen = set()
    curr = head
    prev = None
    
    # iterate through the list
    while curr and curr not in seen:
        seen.add(curr)
        prev = curr
        curr = curr.next
        
    return prev


num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
num4.next = num1
print(find_last_node_in_cycle(num1).value) # type: ignore


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

grade(find_last_node_in_cycle)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([[1, 2, 3, 4], 1], expected=4)   # checks the value your code returns against this example
