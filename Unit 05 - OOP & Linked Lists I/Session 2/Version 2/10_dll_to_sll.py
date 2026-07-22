'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 2
  Problem 10: Double to Single

  Below are the node classes for a singly linked list and a doubly linked
  list. Write a function `dll_to_sll()` that takes in the `head` of a doubly
  linked list as a parameter and recreates it as a singly linked list.

  The function returns the head of the new singly linked list.

  Write your solution for `dll_to_sll` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `dll_to_sll` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class SLLNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class DLLNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

def dll_to_sll(dll_head):
    pass

# DLL: Ice <-> Water <-> Steam
Steam = DLLNode("Steam")
Water = DLLNode("Water", Steam)
Ice = DLLNode("Ice", Water)
Steam.prev = Water
Water.prev = Ice
dll_head = Ice
sll_head = dll_to_sll(dll_head)

#SLL: Ice -> Water -> Steam

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(sll_head))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node DLL")
single_dll = DLLNode("Solo")
result1 = dll_to_sll(single_dll)
print("  expected:", ["Solo"], "| got:", _to_list(result1))

print("Test 2 - empty DLL (head is None)")
result2 = dll_to_sll(None)
print("  expected:", None, "| got:", result2)

print("Test 3 - DLL with duplicate values")
dup_c = DLLNode("X")
dup_b = DLLNode("X", dup_c)
dup_a = DLLNode("X", dup_b)
dup_c.prev = dup_b
dup_b.prev = dup_a
result3 = dll_to_sll(dup_a)
print("  expected:", ["X", "X", "X"], "| got:", _to_list(result3))


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

grade(dll_to_sll)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['Ice', 'Water', 'Steam'], expected=['Ice', 'Water', 'Steam'])   # checks the value your code returns against this example
