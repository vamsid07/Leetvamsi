# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque()
        q.append(root)
        if not root : 
            return ans
        while q : 
            n = len(q)
            for i in range(n) : 
                node = q.popleft() 
                if node.left : 
                    if node.left.left == None and node.left.right == None :
                        ans += node.left.val
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
        return ans