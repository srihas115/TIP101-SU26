# Problem 1: Nested Constructors

Step 1: Copy the following code into your IDE.


Step 2: Add a line of code (outside of the class) to create the linked list `4 -> 3 -> 2` in a single assignment statement.


```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
```


<details>
  <summary>💡 <b>Hint: Nested Constructors</b></summary>

  <br>

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
</details>
