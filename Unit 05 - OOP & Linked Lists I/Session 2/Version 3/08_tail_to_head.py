'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 3
  Problem 8: Move Tail to Front

  Write a function `tail_to_head()` that takes in the `head` of a linked
  list as a parameter, and moves the tail of the linked list to the front.

  Write your solution for `tail_to_head` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `tail_to_head` and its parameters exactly as given —
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

def tail_to_head(head):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# Input: 1 -> 2 -> 3 -> 4
_n4 = Node(4)
_n3 = Node(3, _n4)
_n2 = Node(2, _n3)
_n1 = Node(1, _n2)
result = tail_to_head(_n1)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (unchanged)")
single = Node(9)
result1 = tail_to_head(single)
print("  expected:", [9], "| got:", _to_list(result1))

print("Test 2 - two-node list (swaps the two nodes)")
t2 = Node('B')
t1 = Node('A', t2)
result2 = tail_to_head(t1)
print("  expected:", ['B', 'A'], "| got:", _to_list(result2))

print("Test 3 - list with duplicate values")
d3 = Node('x')
d2 = Node('y', d3)
d1 = Node('x', d2)
result3 = tail_to_head(d1)
print("  expected:", ['x', 'x', 'y'], "| got:", _to_list(result3))


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

grade(tail_to_head)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=[4, 1, 2, 3])   # checks the value your code returns against this example
