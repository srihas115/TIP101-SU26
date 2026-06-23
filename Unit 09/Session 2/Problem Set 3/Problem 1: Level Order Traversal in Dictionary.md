# Problem 1: Level Order Traversal in Dictionary

Given the following pseudocode and the `root` of a binary tree, return a dictionary storing the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).


The dictionary’s key should be an integer representing the level. The corresponding value for each key should be a list of node values in that level from left to right.


Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.


```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_dict(root):
    # If the tree is empty:
    # return an empty dictionary

    # Create an empty dictionary
    # Create an empty queue using deque

    # Append a tuple (root, 1) to the queue. The queue will store tuples of (node, level)

    # While the queue is not empty:
    # Pop the next node, level pair off the queue (pop from the left side!)

    # If the level is not yet a key in the dictionary
    # Add to dictionary with empty list as a value

    # Add a tuple with each of the popped node's children
    # and incremented level to the end of the queue
    pass
```

Example Usage:


```python
Example Input Tree

      4
     / \
    2   6
   / \
  1   3

Example Input: root = 4
Expected Output: {1: [4], 2: [2, 6], 3: [1, 3]}
Explanation:
Level 1: Node 4
Level 2 (left to right): Node 2, Node 6
Level 3 (left to right): Node 1, Node 3
```


### ✨ AI Hint: Breadth First Search Traversal


*Key Skill: Use AI to explain code concepts*


To solve this problem, it may be helpful to understand both the **queue** data structure and **breadth first search** algorithm. To learn more about these concepts, visit the Queues and Breadth First Search sections of the [Unit 9 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/9#!cheatsheet)


If you still have questions, try explaining what you're doing, and ask an AI tool like ChatGPT or GitHub Copilot to help you understand what's confusing you. For example, you might ask:


*"I'm trying to understand how to use a queue to implement breadth first search, but I'm confused about why I wouldn't just use a list. Can you explain the difference?"*
