# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        prev,cur = None, mid
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        d = prev
        first, second = head, d
        while second.next:
            nxt = first.next
            first.next = second
            first = nxt
            
            nxt = second.next
            second.next = first
            second = nxt
            