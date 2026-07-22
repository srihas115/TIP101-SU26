'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 1  ·  Version 3
    Problem 6: Reverse Them, K?

    Given the head of a singly linked list and an integer k, reverse the first
    k elements of the linked list. Return the new head of the linked list. If
    k is larger than the length of the list, reverse the entire list.

    Evaluate the time and space complexity of your solution. Define your
    variables and provide a rationale for why you believe your solution has
    the stated time and space complexity.

    Write your solution for `reverse_first_k` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `reverse_first_k` and its parameters exactly as given —
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

def reverse_first_k(head, k):
    pass

# Input List: 1 —> 2 —> 3 —> 4 —> 5
# Input: head = 1, k = 3
def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

_n5 = Node(5)
_n4 = Node(4, _n5)
_n3 = Node(3, _n4)
_n2 = Node(2, _n3)
_n1 = Node(1, _n2)
result = reverse_first_k(_n1, 3)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(9)
result1 = reverse_first_k(single, 1)
print("  expected:", [9], "| got:", _to_list(result1))

print("Test 2 - k greater than list length (reverses the entire list)")
t3 = Node(3)
t2 = Node(2, t3)
t1 = Node(1, t2)
result2 = reverse_first_k(t1, 100)
print("  expected:", [3, 2, 1], "| got:", _to_list(result2))

print("Test 3 - k is 1 (no visible change)")
u3 = Node(3)
u2 = Node(2, u3)
u1 = Node(1, u2)
result3 = reverse_first_k(u1, 1)
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

grade(reverse_first_k)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], 3, expected=[3, 2, 1, 4, 5])   # checks the value your code returns against this example
