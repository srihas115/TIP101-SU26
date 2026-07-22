class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1

# Time Complexity: O(n)
# Space Complexity: O(1)
def count_element(head, val):
    curr = head
    counter = 0
    
    while curr is not None:
        if curr.value == val:
            counter += 1
        curr = curr.next
    
    print(counter)

# Test
head = Node(3, Node(1, Node(2, Node(1))))
count_element(head, 1)


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

grade(count_element)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 1, 2, 1], 1, expected=2)   # checks the value your code returns against this example
