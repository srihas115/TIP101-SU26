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

# Function with a bug!
def remove_by_value(head, val):
    # Handle empty list and removal from the head
    if not head:
        return None
    if head.value == val:
        return head.next  # Return the second node as the new head

    current = head
    while current.next:
        if current.next.value == val:
            current = current.next.next  # Skip the node with the value
            return head  # Return the original head
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3


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

grade(remove_by_value)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], 3, expected=[1, 2, 4])   # checks the value your code returns against this example
