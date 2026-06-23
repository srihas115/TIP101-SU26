# Problem 1: The Power of One

The following code creates the linked list `Ash -> Misty -> Brock`. Refactor the code to create the same list with a single line of code.


```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# Recreate this list in a single line of code
head = Node("Ash")
misty = Node("Misty")
brock = Node("Brock")
head.next = misty
luigi.next = brock
```


### 💡 Hint: Nested Constructors


This problem requires you to be familiar with nesting constructors. The `Node` class below accepts two parameters:


- the value of the Node object.

- the next Node object in the linked list or `None` if the Node is not linked to another node.


```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
```

In the past, we constructed each node in the list individually, then linked them together.


```python
node_one = Node(1)
node_two = Node(2)
node_one.next = node_two
```

We can instead chain together our constructor calls, and pass in a second Node object `Node(2)` as the `next` argument for the first node.


```python
head = Node(1, Node(2))
```

This technique is commonly used when generating test cases for linked lists.
