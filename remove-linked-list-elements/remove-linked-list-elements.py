# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode(-1)
        d.next = head
        cur = d
        while cur.next!=None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return d.next
        