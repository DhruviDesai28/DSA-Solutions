# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d = t = ListNode(0)
        d.next = head
        for _ in range(left-1):
            t = t.next
        cur = t.next
        prev = None
        for _ in range(right - left+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        t.next.next = cur
        t.next = prev
        return d.next