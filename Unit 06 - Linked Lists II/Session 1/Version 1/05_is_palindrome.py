class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

'''
1. Understand
    input: head
    output: return True if values is palindrome, False otherwise
    core logic: multiple pass technique
        one pointer for traversing the original list, one for traversing the reversed list (or fast/slow pointers for the O(1) space approach).
        
    Edge cases:
    a) Linked List is empty
    b) Linked List has only 1 node

3. Plan
    Idea 1: Find the middle. reverse the 2nd half of the linked list. and check if it is identical to the first half
    Idea 2: create a copy of the original linked list, reverse the copy, and check if the reversed is identical to the original

'''

# Time Complexity: O(n)
# Space Complexity: O(n), because we create a deep copy of the original linked list
def is_palindrome1(head):
    if head is None: # Empty LL
        return True
    if head.next is None: # LL with only 1 node
        return True
    
    # 1. Create a deep copy of the linked list
    copy_head = Node(head.value)
    curr_orig = head.next
    curr_copy = copy_head
    
    while curr_orig:
        curr_copy.next = Node(curr_orig.value)
        curr_orig = curr_orig.next
        curr_copy = curr_copy.next
        
    # 2. Reverse the copied list using the helper
    reversed_copy_head = HELPER_reverse_linked_list(copy_head)
    
    # 3. Compare the original list with the reversed copy
    ptr1 = head
    ptr2 = reversed_copy_head
    
    while ptr1 and ptr2:
        if ptr1.value != ptr2.value:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        
    return True

# Time Complexity: O(n)
# Space Complexity: O(1), we are only using a modified two-pointer approach
def is_palindrome2(head):
    if head is None: # Empty LL
        return True
    if head.next is None: # LL with only 1 node
        return True
    
    # 1. Find the middle of the linked list using fast/slow pointers
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # 2. Reverse the second half starting from the 'slow' pointer
    second_half_head = HELPER_reverse_linked_list(slow)
    
    # 3. Compare the first half and the reversed second half
    ptr1 = head
    ptr2 = second_half_head
    
    # We only need to check until ptr2 runs out (the second half)
    while ptr2:
        if ptr1.value != ptr2.value:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        
    return True

def HELPER_reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next   # temporarily store the next node
        curr.next = prev        # reverse the current node's pointer
        prev = curr             # move the prev pointer forward
        curr = next_node        # move the curr pointer forward
    return prev                 # prev becomes the new head of the reversed list

# Input List:
# 1 -> 2 -> 1
# Input: head = 1
head = Node(1, Node(2, Node(1)))
print("Testing O(n) Space Approach:", is_palindrome1(head)) # Expected: True
print("Testing O(1) Space Approach:", is_palindrome2(head)) # Expected: True

print()

# Additional Test Case
# 1 -> 2 -> 3
head2 = Node(1, Node(2, Node(3)))
print("Testing O(n) Space Approach (False Case):", is_palindrome1(head2)) # Expected: False
print("Testing O(1) Space Approach (False Case):", is_palindrome2(head2)) # Expected: False


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

grade(is_palindrome)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 1], expected=True)   # checks the value your code returns against this example
