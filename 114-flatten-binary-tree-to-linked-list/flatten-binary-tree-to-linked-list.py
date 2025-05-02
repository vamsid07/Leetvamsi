# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: 
            return None 
        st = []
        curr = root 
        prev = None
        while curr: 
            if curr.left: 
                if curr.right:
                    st.append(curr.right)
                curr.right = curr.left
                curr.left = None
            prev = curr
            curr = curr.right
        while len(st) > 0: 
            temp = st.pop()
            curr = temp
            while curr:
                if curr.left: 
                    if curr.right:
                        st.append(curr.right)
                    curr.right = curr.left
                    curr.left = None
                if curr.right is None:
                    break
                curr = curr.right
            prev.right = temp
            prev = curr