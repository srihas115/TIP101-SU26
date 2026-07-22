class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if root is None:  # if tree is empty
        return False
    # if left child is equal to the root and there is only 1 child
    elif (root.right is None) and (root.left) and (root.val == root.left.val):
        return True
    # if right child is equal to the root and there is only 1 child
    elif (root.left is None) and (root.right) and (root.val == root.right.val):
        return True
    # check if the sum of both children is equal to the root
    elif root.left and root.right and root.val == root.left.val + root.right.val:
        return True
    return False
    
# Test Cases:
tree1 = TreeNode(10, TreeNode(10), None)  # only one child
tree2 = TreeNode(5, TreeNode(3), TreeNode(2))
tree3 = TreeNode(5, None, TreeNode(2))
tree4 = TreeNode(None)

print(check_tree(tree1))
print(check_tree(tree2))
print(check_tree(tree3))
print(check_tree(tree4))