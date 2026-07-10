class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

'''
1. understand

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

result:
1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3


create two linked lists: greater or less than the value

'''

def partition(head, val):
    smaller = None
    bigger = None
    curr = 
    
    
    pass

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# small list = 1 -> 2 -> 2
# big list = 4 -> 3 -> 5


# result: 1 -> 2 -> 2 -> 4 -> 3 -> 5 

# head = 1, val = 3

# i really want to work on this later - jessica
