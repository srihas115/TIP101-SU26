'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 1
  Problem 6: Reverse Sublist Between m and n

  Given the head of a linked list and indices `m` and `n`, reverse the
  linked list between positions `m` and `n`. Assume the linked list uses
  **1-based indexing** and the `0 <= m <= n <= length of list`. Return the
  head of the list.

  Write your solution for `reverse_between` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `reverse_between` and its parameters exactly as given —
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

def reverse_between(head, m, n):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# input list: 1 -> 2 -> 3 -> 4 -> 5
_n5 = Node(5)
_n4 = Node(4, _n5)
_n3 = Node(3, _n4)
_n2 = Node(2, _n3)
head = Node(1, _n2)
result = reverse_between(head, 2, 5)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - m equals n (no visible change)")
s5 = Node(5)
s4 = Node(4, s5)
s3 = Node(3, s4)
s2 = Node(2, s3)
s1 = Node(1, s2)
result1 = reverse_between(s1, 3, 3)
print("  expected:", [1, 2, 3, 4, 5], "| got:", _to_list(result1))

print("Test 2 - reverse the entire list (m=1, n=length)")
t3 = Node(3)
t2 = Node(2, t3)
t1 = Node(1, t2)
result2 = reverse_between(t1, 1, 3)
print("  expected:", [3, 2, 1], "| got:", _to_list(result2))

print("Test 3 - reverse a middle sublist not touching either end")
u5 = Node(5)
u4 = Node(4, u5)
u3 = Node(3, u4)
u2 = Node(2, u3)
u1 = Node(1, u2)
result3 = reverse_between(u1, 2, 4)
print("  expected:", [1, 4, 3, 2, 5], "| got:", _to_list(result3))


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

grade(reverse_between)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], 2, 5, expected=[1, 5, 4, 3, 2])   # checks the value your code returns against this example
