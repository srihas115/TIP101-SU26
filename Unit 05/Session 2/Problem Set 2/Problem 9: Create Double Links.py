class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

head = Node("First")
tail = Node("Last")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)
