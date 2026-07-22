'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 3
  Problem 4: Increment Node Values

  Write a function `increment_ll()` that takes in the `head` of a linked
  list of integer values and returns the same list, but with each node's
  value incremented by 1. Return the `head` of the list.

  Write your solution for `increment_ll` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `increment_ll` and its parameters exactly as given —
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

def increment_ll(head):
    pass

# my_list: 5 -> 6 -> 7
_n3 = Node(7)
_n2 = Node(6, _n3)
my_list = Node(5, _n2)
print(my_list.value)

my_list = increment_ll(my_list)
# my_list: 6 -> 7 -> 8
print(my_list.value)

my_list = increment_ll(my_list)
# my_list: 7 -> 8 -> 9
print(my_list.value)

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(10)
result1 = increment_ll(single)
print("  expected:", [11], "| got:", _to_list(result1))

print("Test 2 - all values incremented, full chain")
c3 = Node(3)
c2 = Node(2, c3)
c1 = Node(1, c2)
result2 = increment_ll(c1)
print("  expected:", [2, 3, 4], "| got:", _to_list(result2))

print("Test 3 - negative values")
neg2 = Node(-1)
neg1 = Node(-5, neg2)
result3 = increment_ll(neg1)
print("  expected:", [-4, 0], "| got:", _to_list(result3))


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

grade(increment_ll)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 7], expected=[6, 7, 8])   # checks the value your code returns against this example
