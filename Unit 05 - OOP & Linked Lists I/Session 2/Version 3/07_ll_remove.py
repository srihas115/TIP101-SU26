class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_remove(head, val):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# Linked List: 5 -> 6 -> 7 -> 8
_n4 = Node(8)
_n3 = Node(7, _n4)
_n2 = Node(6, _n3)
_n1 = Node(5, _n2)
result = ll_remove(_n1, 6)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - value not found (list unchanged)")
u2 = Node(2)
u1 = Node(1, u2)
result1 = ll_remove(u1, 99)
print("  expected:", [1, 2], "| got:", _to_list(result1))

print("Test 2 - removing the head")
h2 = Node(2)
h1 = Node(1, h2)
result2 = ll_remove(h1, 1)
print("  expected:", [2], "| got:", _to_list(result2))

print("Test 3 - single-node list, value matches (empties the list)")
single = Node(9)
result3 = ll_remove(single, 9)
print("  expected:", [], "| got:", _to_list(result3))

print("Test 4 - removes only the first matching duplicate")
q3 = Node(5)
q2 = Node(5, q3)
q1 = Node(1, q2)
result4 = ll_remove(q1, 5)
print("  expected:", [1, 5], "| got:", _to_list(result4))


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

grade(ll_remove)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 7, 8], 6, expected=[5, 7, 8])   # checks the value your code returns against this example
