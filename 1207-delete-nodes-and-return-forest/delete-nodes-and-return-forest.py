# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        s = set(to_delete)
        def go(root) : 
            nonlocal ans
            if root is None :
                return None
            root.left = go(root.left)
            root.right = go(root.right)
            if root.val in s : 
                if root.right :
                    ans.append(root.right)
                if root.left :
                    ans.append(root.left)
                return None
            return root 
        go(root)
        if root.val not in s :
            ans.append(root)
        return ans