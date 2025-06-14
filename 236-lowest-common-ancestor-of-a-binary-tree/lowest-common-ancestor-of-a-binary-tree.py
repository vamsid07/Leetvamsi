class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def go(root):
            if not root:
                return None
            left = go(root.left)
            right = go(root.right)
            if root == p or root == q:
                return root
            if left and right:
                return root
            if left : 
                return left 
            return right
        return go(root)
