# Problem 12: Print Linked List

Write a function `print_linked_list()` that takes in a head of a linked list as a parameter. The function prints and returns a list of all the values in the linked list in the order they appear in the linked list.


*Note: The "head" of a linked list is the first element in the linked list, equivalent to `lst[0]` of a normal list.*


```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	pass
```

Example Usage:


```python
# input linked list: a->b->c->d->e
print_linked_list(a)
```

Example Output:


```python
['a','b','c','d','e']
```


### 💡 Hint: Linked List Traversal


This problem requires you to traverse a linked list. In other words, it requires you to iterate over the nodes of a linked list. For a break down of how to traverse a linked list, check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet).
