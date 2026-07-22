'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 3
    Problem 3: Insert Node as Second Element

    Write a function `add_second()` that takes in the `head` of a linked list
    and a value object `val` as parameters. It should insert `val` as the
    second node in the linked list and return the **head** of the linked list.
    (You can assume `head` is not `None`.)

    *Note: The "head" of a linked list is the first element in the linked
    list. Equivalent to `lst[0]` of a normal list.*

    Write your solution for `add_second` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `add_second` and its parameters exactly as given —
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

def add_second(head, val):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# linked list: 1 -> 3 -> 4
n1 = Node(1)
n3 = Node(3)
n4 = Node(4)
n1.next = n3
n3.next = n4
result = add_second(n1, 2)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (new node becomes the second)")
single = Node('a')
result1 = add_second(single, 'b')
print("  expected:", ['a', 'b'], "| got:", _to_list(result1))

print("Test 2 - two-node list")
t2 = Node('y')
t1 = Node('x', t2)
result2 = add_second(t1, 'z')
print("  expected:", ['x', 'z', 'y'], "| got:", _to_list(result2))

print("Test 3 - list with duplicate values")
dup2 = Node('same')
dup1 = Node('same', dup2)
result3 = add_second(dup1, 'same')
print("  expected:", ['same', 'same', 'same'], "| got:", _to_list(result3))


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

grade(add_second)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 4], 2, expected=[1, 2, 3, 4])   # checks the value your code returns against this example
