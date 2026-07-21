class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_node(head, val):
    pass

# Example 1:
# Build: 1 -> 2 -> 3 -> (back to 1)
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
head = num1

head = delete_node(head, 2)
# Result Linked List (by values): 1 -> 3 -> 1
