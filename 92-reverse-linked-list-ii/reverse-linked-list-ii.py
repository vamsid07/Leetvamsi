# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        scurr = head 
        prev = None
        while scurr and count < left: 
            prev = scurr
            scurr = scurr.next 
            count += 1 
        tail = scurr
        subprev = None
        while scurr and count <= right:
            temp = scurr.next
            scurr.next = subprev
            subprev = scurr
            scurr = temp
            count += 1
        if prev:
            prev.next = subprev
        else:
            head = subprev
        tail.next = scurr
        return head
