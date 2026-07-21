# Problem 2: Find Minimum Depth of Binary Tree

Given the `root` of a binary tree, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the `root` down to the nearest leaf node.


Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.


```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def min_depth(root):
	pass
```

Example Usage:


```python
Example Input Tree #1:

   3
  / \
 9  20
    / \
   15  7

Example Input: root = 3
Expected Output: 2
Shortest path from root node to a leaf node is 3 -> 9. Number of nodes in path is 2.

Example Input Tree #2:

   2
    \
     3
      \
       4
        \
         5
          \
           6

Example Input: root = 2
Expected Output: 5
Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6.
Number of nodes in path is 5.
```


<details>
  <summary>💡 <b>Hint: Choosing your Traversal Method</b></summary>

  <br>

This problem can be solved multiple ways, but may work best with a modified breadth first search traversal. To learn more about how to choose a traversal algorithm visit the How to Pick a Traversal Algorithm section of the [Unit 9 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/9#!cheatsheet).
</details>
