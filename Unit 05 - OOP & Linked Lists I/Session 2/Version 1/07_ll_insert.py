'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
  Problem 7: Insert Value

  Write a function `ll_insert()` that takes in a `head` of a linked list, a
  value `val`, and an index `i` as parameters.

  The function should insert a new `Node` with value `val` at index `i` of
  the linked list, then return the head of the linked list. - If `i` is
  greater than the length of the list, insert the new node at the end of the
  list.

  *Hint: Linked lists do not have built-in indices so you will need to track
  the indices yourself.*

  Write a helper function to help you print the new list!

  Write your solution for `ll_insert` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `ll_insert` and its parameters exactly as given —
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

def ll_insert(head, val, i):
    pass

# linked list: 3 -> 8 -> 12 -> 9
n1 = Node(3)
n2 = Node(8)
n3 = Node(12)
n4 = Node(9)
n1.next = n2
n2.next = n3
n3.next = n4
head = n1
new_head = ll_insert(head, 20, 2)

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(new_head))
# result linked list: 3 -> 8 -> 20 -> 12 -> 9

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - insert at index 0 (new head)")
h1 = Node(1)
h1.next = Node(2)
result1 = ll_insert(h1, 99, 0)
print("  expected:", [99, 1, 2], "| got:", _to_list(result1))

print("Test 2 - insert at the end (i equals length)")
h2 = Node(1)
h2.next = Node(2)
result2 = ll_insert(h2, 99, 2)
print("  expected:", [1, 2, 99], "| got:", _to_list(result2))

print("Test 3 - insert into an empty list")
result3 = ll_insert(None, 99, 0)
print("  expected:", [99], "| got:", _to_list(result3))

print("Test 4 - insert into a single-node list")
h4 = Node(5)
result4 = ll_insert(h4, 99, 1)
print("  expected:", [5, 99], "| got:", _to_list(result4))


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

grade(ll_insert)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 8, 12, 9], 20, 2, expected=[3, 8, 20, 12, 9])   # checks the value your code returns against this example
