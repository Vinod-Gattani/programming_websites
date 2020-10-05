# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def getDepth(self, node, data, level, parent_node):
        
        if (node == None): 
            return 0, None

        if (node.val == data) : 
            return level, parent_node
        
        
        downlevel, parent_node = self.getDepth(node.left, 
                                 data, level + 1, node.val)  
        if (downlevel != 0) : 
            return downlevel, parent_node 

        downlevel, parent_node = self.getDepth(node.right,  
                                 data, level + 1, node.val) 

        
        return downlevel, parent_node
    
    #my solution
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        left_depth, left_parent_node = self.getDepth(root, x, 0, 0)
        right_depth, right_parent_node  = self.getDepth(root, y, 0, 0)
        
        return (left_depth==right_depth) and (left_parent_node != right_parent_node)

    #copied
    def isCousins1(self, root, x, y):
       
        lookup = {} #dictionary for maintaining the level and value of the node
        def dfs(root, level=0, value=None):
            if root:
                if root.val in (x, y): 
                    lookup[root.val] = (level, value)
                dfs(root.left, level=level+1, value=root.val)
                dfs(root.right, level=level+1, value=root.val)
        dfs(root)
        return lookup[x][0] == lookup[y][0] and lookup[x][1] != lookup[y][1]
        