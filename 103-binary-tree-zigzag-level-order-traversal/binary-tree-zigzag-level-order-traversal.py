# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        ans = []
        if root == None : 
            return []
        flag = 0
        while q : 
            n = len(q) 
            temp = []
            for i in range(n) :
                node = q.popleft()
                temp.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            if flag == 1 :
                ans.append(temp[::-1])
                flag = 0 
            else :
                ans.append(temp)
                flag = 1
        return ans