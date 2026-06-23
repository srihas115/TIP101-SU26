# Problem 8: Binary Tree Is Leaf

Given a `value` and the `root` of a binary search tree, write a function `is_leaf_bst()` that returns `True` if a node with the given value is a leaf node and `False` otherwise. Assume the tree is balanced.


Evaluate the time complexity of your solution.


```python
# Example Input Tree:
"""
      1
     / \
    /   \
   2     5
  / \
 4   3
"""
# Input: root = 1, value = 5
# Expected Output: True

# Example Input Tree:
"""
      1
     / \
    /   \
   2     5
  /
 4
"""
# Input: root = 1, value = 2
# Expected Output: False


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def is_leaf(root, value):
	pass
```


<details>
  <summary>✨ <b>AI Hint: Balanced Trees</b></summary>

  <br>

Tree problems will often specify whether or not you can assume a tree is balanced. This can affect the time complexity of your algorithm.


For a quick refresher, check out the Balanced Tree section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet). If you need more help, try using an AI tool like ChatGPT or GitHub Copilot to show you examples of balanced trees and how they work. For example, you could ask:


*"You're an expert computer science tutor. Can you help me understand the concept of a balanced binary tree, using multiple examples and an analogy to real-world objects?"*
</details>
