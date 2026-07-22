'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 1  ·  Version 1
    Problem 4: Find the Middle

    A variation of the two-pointer technique introduced in Unit 4 is to have a
    slow and a fast pointer that increment at different rates. Given the head
    of a linked list, use the slow-fast pointer technique to find the middle
    node of a linked list. If there are two middle nodes, return the second
    middle node.

    Evaluate the time and space complexity of your solution. Define your
    variables and provide a rationale for why you believe your solution has
    the stated time and space complexity.

    Write your solution for `find_middle_element` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_middle_element` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic):
input: head
output: middle node,
    if there are two, return the second middle node
core logic:
    iterate through the linked list with slow and fast pointer technique
edge cases:
    head empty, one node
    has two middle nodes (even number of nodes in list)

Match:

Plan:
define slow and fast pointers starting from the head

iterate through the list --> while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

'''


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
