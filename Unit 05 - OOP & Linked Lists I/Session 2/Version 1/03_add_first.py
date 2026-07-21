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
