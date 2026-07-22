'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
    Problem 6: List Nodes

    Write a function `listify_first_n()` that takes in a `head` of a linked
    list and a non-negative integer `n` as parameters.

    The function returns a list of values of the first `n` nodes. - If `n` is
    greater than the length of the linked list, return a list of the values of
    all nodes in the linked list.

    Write your solution for `listify_first_n` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `listify_first_n` and its parameters exactly as given —
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

def listify_first_n(head, n):
    pass

# linked list: a -> b -> c
a = Node('a')
b = Node('b')
c = Node('c')
a.next = b
b.next = c
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l
j = Node('j')
k = Node('k')
l = Node('l')
j.next = k
k.next = l
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (head is None)")
print("  expected:", [], "| got:", listify_first_n(None, 3))

print("Test 2 - n is 0")
print("  expected:", [], "| got:", listify_first_n(a, 0))

print("Test 3 - single-node list")
single = Node('x')
print("  expected:", ['x'], "| got:", listify_first_n(single, 1))

print("Test 4 - n exactly equals the list length")
print("  expected:", ['a', 'b', 'c'], "| got:", listify_first_n(a, 3))


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

grade(listify_first_n)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], 2, expected=[1, 2])   # checks the value your code returns against this example
