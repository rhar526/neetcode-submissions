# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        right = slow.next
        prev, curr = None, right

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        slow.next = None
        left, right = head, prev 

        while left and right:
            lnxt, rnxt = left.next, right.next
            left.next = right
            right.next = lnxt
            left = lnxt
            right = rnxt
        
