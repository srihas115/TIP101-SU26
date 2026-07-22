class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# From Problem 3: Remove Tail.py
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

'''
1. Understand
    input: head
    output: middle node,
        if there are two, return the second middle node
    core logic:
        iterate through the linked list with slow and fast pointer technique
    edge cases:
        head empty, one node
        has two middle nodes (even number of nodes in list)
        [1, 2, 3, 4]     None
                         f
               s
        One more iteration to get to the second middle

3. Plan
    define slow and fast pointers starting from the head

    iterate through the list --> while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
'''

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_middle_element(head):
    slow = head # slow is going to be the middle
    fast = head # fast is going to be after the end (None)
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Input List:
# 1 -> 2 -> 3
# Input: head = 1
head = Node(1, Node(2, Node(3)))
mid = find_middle_element(head)
# print(mid.value) # pyright: ignore[reportOptionalMemberAccess]
if mid:
    print(mid.value)
else:
    print("List is empty")

print()

# 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node(4))))
mid = find_middle_element(head)
# print(mid.value) # pyright: ignore[reportOptionalMemberAccess]
if mid:
    print(mid.value)
else:
    print("List is empty")


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

grade(find_middle_element)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=2)   # checks the value your code returns against this example
