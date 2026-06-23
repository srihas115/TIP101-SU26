# Problem 8: Binary Tree Find

Given a `value` and the `root` of a tree, write a function `find()` that returns `True` if there is a node with the given `value` in the tree. Assume the tree is balanced.


Evaluate the time complexity of your solution.


```python
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def find(root, value):
	pass
```


```python
Example Input Tree #1:

      1
     / \
    /   \
   2     5
  / \
 4   3

Input: root = 1, value = 5
Expected Output: True

Example Input Tree #2:

      1
     / \
    /   \
   2     5
  / \
 4   3

Input: root = 1, value = 10
Expected Output: False
```


### ✨ AI Hint: Balanced Trees


Tree problems will often specify whether or not you can assume a tree is balanced. This can affect the time complexity of your algorithm.


For a quick refresher, check out the Balanced Tree section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet). If you need more help, try using an AI tool like ChatGPT or GitHub Copilot to show you examples of balanced trees and how they work. For example, you could ask:


*"You're an expert computer science tutor. Can you help me understand the concept of a balanced binary tree, using multiple examples and an analogy to real-world objects?"*
