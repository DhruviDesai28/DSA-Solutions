# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        t = ListNode(0)
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        c = slow
        x = c
        prev = None
        while c:
            nxt = c.next
            c.next= prev
            prev = c
            c = nxt
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True