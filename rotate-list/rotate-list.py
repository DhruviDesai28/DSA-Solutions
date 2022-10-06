# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        cur = head
        c = 1
        while cur.next:
            cur = cur.next
            c+=1
        k = k%c
        cur.next = head
        d = head
        for _ in range(c-k-1):
            d=d.next
        ans = d.next
        d.next = None
        return ans
        