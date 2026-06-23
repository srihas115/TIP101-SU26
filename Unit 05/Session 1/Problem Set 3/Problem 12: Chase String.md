# Problem 12: Chase String

Write a function `chase_list()` that takes in a head of a linked list and returns a string linking together the **values** of the list with the separator `"chases"`.


*Note: The "head" of a linked list is the first element in the linked list. Equivalent to `lst[0]` of a normal list.*


Example Usage:


```python
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))
```

Example Output: `"Spike chases Tom chases Jerry chases Gouda"`


### 💡 Hint: Linked List Traversal


This problem requires you to traverse a linked list. In other words, it requires you to iterate over the nodes of a linked list. For a break down of how to traverse a linked list, check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet).
