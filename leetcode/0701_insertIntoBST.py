Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        to_add_node = TreeNode(val)
        
        current_node = root
        
        while current_node:
            y = current_node
            if val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
                
        if val < y.val:
            y.left = to_add_node
        else:
            y.right = to_add_node
        
        return root