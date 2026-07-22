'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 1  ·  Version 1
  Problem 3: Remove Tail

  The following code attempts to remove the tail of a singly linked list.
  However, it has a bug!

  Step 1: Copy this code into your IDE.

  Step 2: Create your own test cases to run the code against, and use print
  statements and the stack trace to identify and fix the bug so that the
  function correctly removes the tail of the list.

  Write your solution for `remove_tail` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `remove_tail` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug!
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None

    # Start from the head and find the second-to-last node
    current = head
    while current.next.next is not None:
        # print(current.value)
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
head = Node(1, Node(2, Node(3, Node(4))))
remove_tail(head)
print_list(head)

print()

two_nodes = Node(1, Node(2))
remove_tail(two_nodes)
print_list(two_nodes)


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

grade(remove_tail)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=[1, 2, 3])   # checks the value your code returns against this example
