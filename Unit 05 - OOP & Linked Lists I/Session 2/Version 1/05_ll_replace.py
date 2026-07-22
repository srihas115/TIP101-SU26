'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
  Problem 5: Replace Node

  Using the `Node` class, write a function `ll_replace()` that updates in
  place every node whose `value == original` to have `value = replacement`.
  The function returns `None`.

  Write your solution for `ll_replace` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `ll_replace` and its parameters exactly as given —
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

def ll_replace(head, original, replacement):
    if head is None: # linked list is empty
        return None
    if head.next is None: # linked list has only 1 element
        if head.value == original:
            head.value = replacement
    # edge cases ^^
    
    curr = head
    while curr is not None:
        if curr.value == original:
            curr.value = replacement
        curr = curr.next


def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print(to_string(head))


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

grade(ll_replace)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 5], 5, 'banana', expected=['banana', 6, 'banana'])   # checks the updated first argument against this example
