# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # level = 0 
        # if not root : 
        #     return 0
        # q = deque()
        # q.append(root)
        # while q : 
        #     n = len(q)
        #     for i in range(n) : 
        #         node = q.popleft() 
        #         if node.left : 
        #             q.append(node.left)
        #         if node.right : 
        #             q.append(node.right)
        #     level += 1 
        # return level
        def go(root) : 
            if not root : 
                return 0 
            l = go(root.left)
            r = go(root.right)
            return 1 + max(l,r)
        return go(root)