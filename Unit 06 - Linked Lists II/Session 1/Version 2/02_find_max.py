'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 1  ·  Version 2
    Problem 2: Find Max

    Given the head of a linked list where each node is an integer value,
    return the maximum value in the linked list.

    Write your solution for `find_max` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_max` and its parameters exactly as given —
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

def find_max(head):
    pass

# Linked List: 5 -> 6 -> 7 -> 8
# Input: head = 5
_n4 = Node(8)
_n3 = Node(7, _n4)
_n2 = Node(6, _n3)
_n1 = Node(5, _n2)
print(find_max(_n1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(42)
print("  expected:", 42, "| got:", find_max(single))

print("Test 2 - all negative numbers")
neg2 = Node(-1)
neg1 = Node(-5, neg2)
print("  expected:", -1, "| got:", find_max(neg1))

print("Test 3 - duplicate max values")
dup3 = Node(7)
dup2 = Node(7, dup3)
dup1 = Node(3, dup2)
print("  expected:", 7, "| got:", find_max(dup1))


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

grade(find_max)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 7, 8], expected=8)   # checks the value your code returns against this example
