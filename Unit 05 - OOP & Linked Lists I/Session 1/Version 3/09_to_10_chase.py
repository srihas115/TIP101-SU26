class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# From Problem 9:
mouse = Node("Jerry")
cat = Node("Tom", mouse)

# Problem 10: add dog so the list is dog -> cat -> mouse
dog = Node("Spike", cat)

print(dog.value)
print(dog.next.value)
print(dog.next.next.value)
print(cat.value)
print(cat.next.value)
print(mouse.next)

# --- Merged from Problem 10: Chase List.py ---
print(dog.value)
print(dog.next is cat)
print(dog.next.value)
print(cat.next is mouse)
print(cat.next.value)
print(mouse.next)
