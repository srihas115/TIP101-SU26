# Problem 4: Increment Linked List Node Values

Write a function `increment_ll()` that takes in the `head` of a linked list of integer values and returns the same list, but with each node's value incremented by 1. Return the `head` of the list.


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def increment_ll(head):
    pass
```

Example Usage:


```python
# my_list: 5 -> 6 -> 7
print(my_list.value)

my_list = increment_ll(my_list)
# my_list: 6 -> 7 -> 8
print(my_list.value)

my_list = increment_ll(my_list)
# my_list: 7 -> 8 -> 9
print(my_list.value)
```

Example Output:


```python
5
6
7
```


### 💡 Hint: Linked List Traversal


This problem requires you to traverse a linked list. In other words, it requires you to iterate over the nodes of a linked list. For a break down of how to traverse a linked list, check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet).
