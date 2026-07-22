'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 3
  Problem 12: Chase String

  Write a function `chase_list()` that takes in a head of a linked list and
  returns a string linking together the **values** of the list with the
  separator `"chases"`.

  *Note: The "head" of a linked list is the first element in the linked
  list. Equivalent to `lst[0]` of a normal list.*

  Example Usage:

  Write your solution for `chase_list` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `chase_list` and its parameters exactly as given —
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

def chase_list(head):
    pass

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (no 'chases' separator needed)")
single = Node("Spike")
print("  expected:", "Spike", "| got:", chase_list(single))

print("Test 2 - two-node list")
n1 = Node("A")
n2 = Node("B")
n1.next = n2
print("  expected:", "A chases B", "| got:", chase_list(n1))

print("Test 3 - empty list (head is None)")
print("  expected:", "", "| got:", chase_list(None))

print("Test 4 - list with duplicate values")
d1 = Node("X")
d2 = Node("X")
d3 = Node("X")
d1.next = d2
d2.next = d3
print("  expected:", "X chases X chases X", "| got:", chase_list(d1))


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

grade(chase_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['Spike', 'Tom', 'Jerry', 'Gouda'], expected='Spike chases Tom chases Jerry chases Gouda')   # checks the value your code returns against this example
