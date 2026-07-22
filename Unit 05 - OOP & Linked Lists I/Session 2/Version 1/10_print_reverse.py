'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
    Problem 10: Print Backwards

    Write a function `print_reverse()` that takes in the `tail` of a doubly
    linked list as a parameter.

    It should print out the values of the linked list in reverse order, each
    separated by a space.

    Write your solution for `print_reverse` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `print_reverse` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class Node:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail):
    pass

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl", prev=poliwag)
poliwag.next = poliwhirl
poliwrath = Node("Poliwrath", prev=poliwhirl)
poliwhirl.next = poliwrath
print_reverse(poliwrath)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node("Alone")
print("  expected printed output: Alone")
print_reverse(single)

print("Test 2 - two-node list")
tn1 = Node("A")
tn2 = Node("B", prev=tn1)
tn1.next = tn2
print("  expected printed output: B A")
print_reverse(tn2)

print("Test 3 - list with duplicate values")
d1 = Node("X")
d2 = Node("X", prev=d1)
d1.next = d2
d3 = Node("X", prev=d2)
d2.next = d3
print("  expected printed output: X X X")
print_reverse(d3)


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

grade(print_reverse)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected='3 2 1')   # checks the printed output against this example
