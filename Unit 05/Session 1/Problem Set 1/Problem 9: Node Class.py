# UPI
# Understand: make two nodes and assign values to them 
# Plan: create node objects
# Implement: (below)
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_one = Node("a")
node_two = Node("b")

print(node_one.value)
print(node_one.next)
print(node_two.value)
print(node_two.next)
