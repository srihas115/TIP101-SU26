class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n)
# Space: O(n) - there is recursive call stack
def left_most(root):
    if root == None:  # base case: empty tree
        return None    
    elif root.left is None:
        return root.val 

    return left_most(root.left)

# test cases
tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), 5)  # expected: 4
tree2 = TreeNode(1, None, TreeNode(2, 3, None))  # expected: 1
tree3 = TreeNode(None)  # expected: none
tree4 = TreeNode(1, None, TreeNode(5))  # expected: 1

print(left_most(tree1))
print(left_most(tree2))
print(left_most(tree3))
print(left_most(tree4))

# time complexity: O(n)
    # best case: O(1)
    # worst case: O(n)
# space complexity: O(n)