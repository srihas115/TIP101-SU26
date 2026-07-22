'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
    Problem 3: Add First

    Write a function `add_first()` that takes in a `head` of a linked list and
    a `new_node` from the `Node` class as parameters.

    It should insert `new_node` as the new **head** of the linked_list. The
    function returns `new_node`.

    *Note: The "head" of a linked list is the first element in the linked
    list. Equivalent to `lst[0]` of a normal list.*

    Write your solution for `add_first` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `add_first` and its parameters exactly as given —
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


def add_first(head, new_node):
    new_node.next = head
    head = new_node
    
    return new_node

node_1 = Node("Jigglypuff", None)
node_2 = Node("Wigglytuff")
node_1.next = node_2

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)


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

grade(add_first)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], 0, expected=[0, 1, 2, 3])   # checks the value your code returns against this example
