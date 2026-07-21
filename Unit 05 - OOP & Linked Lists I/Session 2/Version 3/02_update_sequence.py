class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

red = Node('red')
yellow = Node('yellow')
blue = Node('blue')
red.next = yellow
yellow.next = blue
