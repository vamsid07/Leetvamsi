"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None : 
            return None
        st = []
        curr = head 
        while curr : 
            if curr.child : 
                if curr.next :
                    st.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr 
                curr.child = None
            elif curr.next == None and len(st) > 0 : 
                temp = st.pop()
                curr.next = temp
                temp.prev = curr
            curr = curr.next 
        return head 