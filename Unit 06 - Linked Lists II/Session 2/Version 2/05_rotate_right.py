'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 2
  Problem 5: Rotate Right by k

  Given the head of a linked list and a non-negative integer `k`, rotate the
  list to the right by `k` places. Return the head of the linked list.

  Write your solution for `rotate_right` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `rotate_right` and its parameters exactly as given —
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


def rotate_right(head, k):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# num1 -> num2 -> num3 -> num4 -> num5
num5 = Node(5)
num4 = Node(4, num5)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
new_head = rotate_right(num1, 2)
print(_to_list(new_head))

# num1 -> num2 -> num3, k greater than list length
m3 = Node(3)
m2 = Node(2, m3)
m1 = Node(1, m2)
new_head2 = rotate_right(m1, 4)
print(_to_list(new_head2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(9)
result1 = rotate_right(single, 3)
print("  expected:", [9], "| got:", _to_list(result1))

print("Test 2 - k is 0 (no rotation)")
z2 = Node('B')
z1 = Node('A', z2)
result2 = rotate_right(z1, 0)
print("  expected:", ['A', 'B'], "| got:", _to_list(result2))

print("Test 3 - k equals the list length (unchanged)")
e3 = Node(3)
e2 = Node(2, e3)
e1 = Node(1, e2)
result3 = rotate_right(e1, 3)
print("  expected:", [1, 2, 3], "| got:", _to_list(result3))


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

grade(rotate_right)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], 2, expected=[4, 5, 1, 2, 3])   # checks the value your code returns against this example
