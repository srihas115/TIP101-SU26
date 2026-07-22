class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_two_lists(head_a, head_b):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# List 1: 1 -> 2 -> 4, List 2: 2 -> 3 -> 4
_a3 = Node(4)
_a2 = Node(2, _a3)
head_a = Node(1, _a2)

_b3 = Node(4)
_b2 = Node(3, _b3)
head_b = Node(2, _b2)

result = merge_two_lists(head_a, head_b)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - one empty list")
single = Node(1)
result1 = merge_two_lists(None, single)
print("  expected:", [1], "| got:", _to_list(result1))

print("Test 2 - both empty lists")
result2 = merge_two_lists(None, None)
print("  expected:", [], "| got:", _to_list(result2))

print("Test 3 - duplicate values across both lists")
dupb2 = Node(1)
dupb1 = Node(1, dupb2)
dupa2 = Node(1)
dupa1 = Node(1, dupa2)
result3 = merge_two_lists(dupa1, dupb1)
print("  expected:", [1, 1, 1, 1], "| got:", _to_list(result3))


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

grade(merge_two_lists)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 4], [1, 3, 4], expected=[1, 1, 2, 3, 4, 4])   # checks the value your code returns against this example
