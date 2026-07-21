# Problem 4: Level Order Traversal of Binary Tree with Nested Lists

Given the `root` of a binary tree, write a function `level_order()` that returns the level order traversal of its nodes’ values (i.e., from left to right, level by level). `level_order()` should return a list of lists, where each inner list contains the node values of a single level in the tree.


Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.


```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
	pass
	
```

Example Usage:


```python
Example Input Tree
     3
    / \
   9  20
      / \
     15  7

Input: root = 3
Expected Output: [ [3], [9, 20], [15, 7]]
```


<details>
  <summary>✨ <b>AI Hint: Nested lists</b></summary>

  <br>

To solve this problem, you will need to return a nested list. To learn more about nested lists - also called **two-dimensional lists** - try using an AI tool like ChatGPT or GitHub Copilot to explain the topic, both conceptually and with examples in Python.
</details>
