# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        temp = float('-inf')
        def go(root) : 
            nonlocal ans
            if root is None : 
                return 0 
            left = go(root.left)
            right = go(root.right)
            res = root.val + left + right
            ans = max(ans,(temp - res)*res)
            return root.val + left + right
        temp = go(root)
        go(root)
        return ans%1000000007