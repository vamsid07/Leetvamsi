# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def go(root) : 
            if root == None : 
                return []
            go(root.left)
            res.append(root.val)
            go(root.right)
            return res
        return go(root)