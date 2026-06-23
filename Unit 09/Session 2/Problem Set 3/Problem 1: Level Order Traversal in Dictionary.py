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
