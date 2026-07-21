class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next= next

def print_linked_list(head):
    curr = head
    while curr is not None:
        if curr.next is not None:
            print(curr.value, end=" -> ")
        else:
            print(curr.value)
        curr = curr.next
            

# input linked list: a->b->c->d->e

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
a.next = b
b.next = c
c.next = d
d.next = e

print_linked_list(a)
