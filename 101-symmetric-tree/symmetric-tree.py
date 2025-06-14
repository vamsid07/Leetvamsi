# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def go(root1,root2) : 
            if root1 == None and root2 : 
                return False
            if root2 == None and root1 : 
                return False 
            if root1 == None and root2 == None : 
                return True
            if root1.val != root2.val : 
                return False 
            return go(root1.left,root2.right) and go(root1.right,root2.left)
        if root == None : 
            return True 
        if root.left and root.right : 
            return go(root.left,root.right)
        if root.left == None and root.right == None : 
            return True
        return False