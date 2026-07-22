class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_nodes(head):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# Input: 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
_v1 = [0, 3, 1, 0, 4, 5, 2, 0]
_nodes1 = [Node(x) for x in _v1]
for _i in range(len(_nodes1) - 1):
    _nodes1[_i].next = _nodes1[_i + 1]
result1 = merge_nodes(_nodes1[0])
print(_to_list(result1))

# Input: 0 -> 1 -> 0 -> 3 -> 0 -> 2 -> 2 -> 0
_v2 = [0, 1, 0, 3, 0, 2, 2, 0]
_nodes2 = [Node(x) for x in _v2]
for _i in range(len(_nodes2) - 1):
    _nodes2[_i].next = _nodes2[_i + 1]
result2 = merge_nodes(_nodes2[0])
print(_to_list(result2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single segment between the head and tail zeros")
_v3 = [0, 5, 0]
_nodes3 = [Node(x) for x in _v3]
for _i in range(len(_nodes3) - 1):
    _nodes3[_i].next = _nodes3[_i + 1]
result3 = merge_nodes(_nodes3[0])
print("  expected:", [5], "| got:", _to_list(result3))

print("Test 2 - multiple single-node segments")
_v4 = [0, 1, 0, 2, 0, 3, 0]
_nodes4 = [Node(x) for x in _v4]
for _i in range(len(_nodes4) - 1):
    _nodes4[_i].next = _nodes4[_i + 1]
result4 = merge_nodes(_nodes4[0])
print("  expected:", [1, 2, 3], "| got:", _to_list(result4))


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

grade(merge_nodes)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([0, 3, 1, 0, 4, 5, 2, 0], expected=[4, 11])   # checks the value your code returns against this example
