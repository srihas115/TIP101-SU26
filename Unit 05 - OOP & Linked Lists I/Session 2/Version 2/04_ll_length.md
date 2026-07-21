# Problem 4: Linked List Length

Write a function `ll_length()` that takes in a `head` of a linked list as a parameter and returns the length of the linked list.


```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def ll_length(head):
	pass
```

Example Usage:


```python
# Linked List: num1 -> num2 -> num3
head = num1
print(ll_length(head))

# Empty Linked List
head = None
print(ll_length(head))
```

Example Output:


```python
3
0
```


<details>
  <summary>💡 <b>Hint: Linked List Traversal</b></summary>

  <br>

This problem requires you to traverse a linked list. In other words, it requires you to iterate over the nodes of a linked list. For a break down of how to traverse a linked list, check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet).
</details>
