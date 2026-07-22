class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head
    
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next   # temporarily store the next node
        curr.next = prev        # reverse the current node's pointer
        prev = curr             # move the prev pointer forward
        curr = next_node        # move the curr pointer forward
    return prev                 # prev becomes the new head of the reversed list

# Taken from Problem 3: Remove Tail.py
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
head = Node(1, Node(2, Node(3, Node(4))))
reversed_head = reverse(head)
print_list(reversed_head)


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

grade(reverse)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=[4, 3, 2, 1])   # checks the value your code returns against this example
