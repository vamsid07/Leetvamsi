# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def go(p,q) : 
            if p and not q : 
                return False 
            if q and not p : 
                return False 
            if not p and not q : 
                return True 
            if p.val != q.val : 
                return False
            return go(p.left,q.left) and go(p.right,q.right)
        return go(p,q)