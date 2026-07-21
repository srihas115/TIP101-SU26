class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_length(head):
    pass

# Linked List: num1 -> num2 -> num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
head = num1
print(ll_length(head))

# Empty Linked List
head = None
print(ll_length(head))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(9)
print("  expected:", 1, "| got:", ll_length(single))

print("Test 2 - longer list")
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
print("  expected:", 5, "| got:", ll_length(n1))
