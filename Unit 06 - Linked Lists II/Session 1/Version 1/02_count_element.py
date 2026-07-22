'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 1  ·  Version 1
    Problem 2: Find Frequency

    Given the `head` of a linked list and a value `val`, return the frequency
    of `val` in the list. Evaluate the time and space complexity of your
    solution. Define your variables and provide a rationale for why you
    believe your solution has the stated time and space complexity.

    Write your solution for `count_element` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `count_element` and its parameters exactly as given —
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
