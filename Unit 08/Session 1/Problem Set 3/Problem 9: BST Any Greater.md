# Problem 9: BST Any Greater

Given a `value` and the `root` of a binary search tree, write a function `contains_greater_bst()` which returns `True` if any nodes greater than `value` exist in the tree. If no node greater than `value` exists, return `False`. Assume the tree is balanced.


Evaluate the time complexity of your solution.


```python
# Example Input Tree:
"""
      4
     / \
    /   \
   2     5
  / \
 1   3
"""
# Input: root = 4, value = 3
# Expected Output:  True

# Example Input Tree:
"""
      4
     / \
    /   \
   2     5
  / \
 1   3
"""
# Input: root = 4, value = 10
# Expected Output: False


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def contains_greater_bst(root, value):
	pass
```


<details>
  <summary>✨ <b>AI Hint: Binary Search Trees</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to be familiar with binary search trees (BSTs). This data structure is incredibly useful, and is often used in many coding interviews.


For a refresher on this topic, check out the Binary Search Tree section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet).


To go deeper, you can ask an AI tool like ChatGPT or GitHub Copilot to explain the concept of binary search trees, how they work, and how to implement them in Python. You can also visit the [VisuAlgo BST Visualizer](https://visualgo.net/en/bst) to see how binary search trees work visually.
</details>
