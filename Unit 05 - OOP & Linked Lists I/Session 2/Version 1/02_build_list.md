# Problem 2: Convert to Linked List

A **linked list** is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.


In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.


In a linked list, the individual elements called **nodes** are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.


Using the provided `Node` class below, create the normal Python list `["Jigglypuff", "Wigglytuff"]` as a linked list.


```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
```

Example Usage (*after completing the problem with variable names `node_1` and `node_2`*):


```python
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
```

Example Output:


```python
Jigglypuff -> Wigglytuff
Wigglytuff -> None
```

Result Linked list: `Jigglypuff -> Wigglytuff`


<details>
  <summary>✨ <b>AI Hint: Linked Lists</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This question requires you to be familiar with Linked Lists, a incredibly useful but sometimes tricky data structure. To help, we've included a review of linked lists [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)


You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Can you help me understand linked lists conceptually, using analogies to real-world objects?"*


Once you understand the concept of Linked Lists, you can also ask follow-up questions like:


*"Can you provide examples of how to implement a linked list in Python, and explain how each part works?"*


*"Here is a provided Linked List class: (CODE). Can you give me an example of how to access the data in this linked list?"*
</details>
