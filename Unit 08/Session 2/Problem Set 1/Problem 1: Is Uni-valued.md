# Problem 1: Is Uni-valued

A binary tree is uni-valued if every node in the tree has the same value. Given the `root` of a binary tree, return `True` if the given tree is uni-valued and `False` otherwise.


Evaluate the time complexity of your solution.


```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_univalued(root):
	pass
```

Example Usage:


```python
Example Input Tree #1

      1
     / \
    /   \
   1     1
  / \     \
 1   1     1

Input: root = 1
Expected Output: True

Example Input Tree #2

      1
     / \
    /   \
   1     2
  / \     \
 1   1     1

Input: root = 1
Expected Output: False
```


<details>
  <summary>✨ <b>AI Hint: Binary Trees</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to understand binary trees. For a refresher on this topic, check out the Binary Trees section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet).


If you need more help, try asking an AI tool like ChatGPT or GitHub Copilot to explain the concept of binary trees using a real-world analogy, and any following questions you have.


Once you grasp the idea, you can ask it to show you examples of binary trees in Python.
</details>
