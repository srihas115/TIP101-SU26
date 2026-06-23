# Problem 2: Collect Nodes of a Cycle in a Linked List

Given the `head` of a linked list, return the elements of any cycle in the linked list as a list.


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_cycle_nodes(head):
	pass
```

Example Usage


```python
# num1 -> num2 -> num3 -> num4 -> num2
lst = collect_cycle_nodes(num1)
print(lst)

# var1 -> var2 -> var3 -> var4
lst2 = collect_cycle_nodes(var1)
print(lst2)
```

Example Output:


```python
[num2, num3, num4]
[]
```


### ✨ AI Hint: Multiple Pass Technique


*Key Skill: Use AI to explain code concepts*


This problem may require multiple traversals of the list. For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/6#!cheatsheet).


For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the multiple pass technique.
