# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def go(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            root.left = go(preorder[1:index+1], inorder[:index])
            root.right = go(preorder[index+1:], inorder[index+1:])
            return root
        return go(preorder, inorder)