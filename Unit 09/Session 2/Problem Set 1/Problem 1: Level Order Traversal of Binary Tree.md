# Problem 1: Level Order Traversal of Binary Tree

Given the following pseudocode and the `root` of a binary tree, return a list of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).


Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.


```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes

    # Add the root to the queue

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes

    # Add each of the popped node's children to the end of the queue

    # Return the list of visited nodes
    pass
```

Example Usage:


```python
Example Input Tree:

      4
     / \
    2   6
   / \
  1   3

Example Input: root = 4
Expected Output: [4, 2, 6, 1, 3]
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
