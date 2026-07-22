class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    pass

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)


# This prints ONLY the head node's value:
print(linked_list.value)   # => "Betty"

# (Optional) Traverse to print the whole linked list:
current = linked_list
while current:
    end_arrow = " -> " if current.next else "\n"
    print(current.value, end=end_arrow)
    current = current.next


# Print the head node's VALUE:
print(linked_list.value)        # expected: Betty

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print("Test 1 - empty list")
print("  expected:", None, "| got:", list_to_linked_list([]))

print("Test 2 - single-element list")
result2 = list_to_linked_list(["Betty"])
print("  expected:", ["Betty"], "| got:", _to_list(result2))

print("Test 3 - list with duplicate values")
result3 = list_to_linked_list(["X", "X", "X"])
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

grade(list_to_linked_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['Betty', 'Veronica', 'Archie', 'Jughead'], expected=['Betty', 'Veronica', 'Archie', 'Jughead'])   # checks the value your code returns against this example
