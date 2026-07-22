'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 1  ·  Version 2
  Problem 5: Where Do We Begin?

  A linked list contains a cycle if the tail element points back to another
  element in the list. Given the head of a linked list, use the fast and
  slow pointer method to determine the node where the cycle starts. If the
  linked list does not contain a cycle, return `None`.

  Evaluate the time and space complexity of your solution. Define your
  variables and provide a rationale for why you believe your solution has
  the stated time and space complexity.

  Write your solution for `get_loop_start` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `get_loop_start` and its parameters exactly as given —
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

def get_loop_start(head):
    pass

# Input List:
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |---------|
# Input: head = 1
_n1 = Node(1)
_n2 = Node(2)
_n3 = Node(3)
_n4 = Node(4)
_n1.next = _n2
_n2.next = _n3
_n3.next = _n4
_n4.next = _n2  # cycle back to node 2
result = get_loop_start(_n1)
print(result.value if result else None)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - non-cyclic list (should NOT be falsely flagged as cyclic)")
nc3 = Node(3)
nc2 = Node(2, nc3)
nc1 = Node(1, nc2)
print("  expected:", None, "| got:", get_loop_start(nc1))

print("Test 2 - single-node self-cycle")
self_node = Node(9)
self_node.next = self_node
result2 = get_loop_start(self_node)
print("  expected:", 9, "| got:", result2.value if result2 else None)

print("Test 3 - empty list (head is None, not cyclic)")
print("  expected:", None, "| got:", get_loop_start(None))


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

grade(get_loop_start)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([[1, 2, 3, 4], 1], expected=2)   # checks the value your code returns against this example
