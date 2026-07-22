'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 2
    Problem 7: Pop Node

    Write a function `ll_pop()` that takes in the `head` of a linked list and
    an index `i` as parameters.

    The function should remove the node at index `i` of the linked list and
    return the `head` of the list. - If `i` is greater than the length of the
    list, do nothing.

    *Hint: Linked lists do not have built-in indices so you will need to track
    the indices yourself.*

    Write your solution for `ll_pop` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `ll_pop` and its parameters exactly as given —
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

def ll_pop(head, i):
    pass

# linked list: num1 -> num2 -> num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
new_head = ll_pop(num1, 1)
# result: num1 -> num3

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(new_head))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - pop index 0 (removes the head)")
p3 = Node(3)
p2 = Node(2, p3)
p1 = Node(1, p2)
result1 = ll_pop(p1, 0)
print("  expected:", [2, 3], "| got:", _to_list(result1))

print("Test 2 - index greater than length (does nothing)")
q2 = Node(2)
q1 = Node(1, q2)
result2 = ll_pop(q1, 10)
print("  expected:", [1, 2], "| got:", _to_list(result2))

print("Test 3 - single-node list, pop index 0 (empties the list)")
s1 = Node(9)
result3 = ll_pop(s1, 0)
print("  expected:", [], "| got:", _to_list(result3))


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

grade(ll_pop)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], 1, expected=[1, 3])   # checks the value your code returns against this example
