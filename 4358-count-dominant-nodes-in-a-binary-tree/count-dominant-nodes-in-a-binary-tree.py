# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0 
        def go(root) :
            nonlocal count
            if not root : 
                return -1
            left = go(root.left) 
            right = go(root.right)
            if not left : 
                return -1
            if not right: 
                return -1 
            if root and (left and root.val >= left ) and (right and root.val >= right ) :
                count += 1 
            return max(root.val,left,right) 
        go(root)

        return count