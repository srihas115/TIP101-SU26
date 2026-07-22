'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 2  ·  Version 3
    Problem 1: Circular List Length

    A circular linked list is a linked list where the tail node points at the
    head node. Write a function that returns the length of the list.

    Evaluate the time and space complexity of your solution. Define your
    variables and provide a rationale for why you believe your solution has
    the stated time and space complexity.

    Write your solution for `circular_list_length` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `circular_list_length` and its parameters exactly as given —
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

def circular_list_length(head):
    pass

# Input List: 1 -> 2 -> 3 -> 1 (circular)
c3 = Node(3)
c2 = Node(2, c3)
c1 = Node(1, c2)
c3.next = c1
print(circular_list_length(c1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node circular list (self-loop)")
self_node = Node(9)
self_node.next = self_node
print("  expected:", 1, "| got:", circular_list_length(self_node))

print("Test 2 - longer circular list")
d5 = Node(5)
d4 = Node(4, d5)
d3 = Node(3, d4)
d2 = Node(2, d3)
d1 = Node(1, d2)
d5.next = d1
print("  expected:", 5, "| got:", circular_list_length(d1))


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

grade(circular_list_length)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=3)   # checks the value your code returns against this example
