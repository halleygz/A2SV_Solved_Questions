# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        it = head
        itp = None
        while(it):
            itn = it.next
            it.next = itp
            itp = it
            it = itn
        return itp