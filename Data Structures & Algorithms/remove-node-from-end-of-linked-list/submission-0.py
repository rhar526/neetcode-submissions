# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        prev1, curr1 = None, head
        
        while curr1:
            next1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = next1
        
        newHead = prev1
        prev2, curr2 = None, prev1
        count = 1

        while count < n:
            prev2 = curr2
            curr2 = curr2.next
            count += 1
        
        if not prev2:
            newHead = curr2.next
        else:
            prev2.next = curr2.next
        
        prev3, curr3 = None, newHead

        while curr3:
            next3 = curr3.next
            curr3.next = prev3
            prev3 = curr3
            curr3 = next3
        
        return prev3


