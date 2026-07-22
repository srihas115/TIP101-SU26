'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 2
    Problem 3: Insert Value First

    Using the `Node` class, write a function `add_first()` that takes in the
    `head` of a linked list and a value object `val` as parameters.

    The function should insert a new `Node` object with value `val` as the new
    **head** of the linked list and return the new node.

    *Note: The "head" of a linked list is the first element in the linked
    list. Equivalent to lst[0] of a normal list.*

    Write your solution for `add_first` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `add_first` and its parameters exactly as given —
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


def add_first(head, val):
    pass

# Linked List: A -> B -> C
node_c = Node('C')
node_b = Node('B', node_c)
node_a = Node('A', node_b)
new_list = add_first(node_a, 0)
# New List: 0 -> A -> B -> C

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(new_list))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (head is None)")
result1 = add_first(None, 99)
print("  expected:", [99], "| got:", _to_list(result1))

print("Test 2 - single-node list")
single = Node('X')
result2 = add_first(single, 'Y')
print("  expected:", ['Y', 'X'], "| got:", _to_list(result2))

print("Test 3 - longer list, chain preserved")
result3 = add_first(node_a, -1)
print("  expected:", [-1, 'A', 'B', 'C'], "| got:", _to_list(result3))


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

grade(add_first)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], 0, expected=[0, 1, 2, 3])   # checks the value your code returns against this example
