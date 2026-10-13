# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        current = head
        pre = head
        nex = head
        # 
        while current is not None:
            nex = current.next
            if current == pre:
                current.next = None
            else:
                current.next = pre
                pre = current
            current = nex
        return pre