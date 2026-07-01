# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        s, f = head, head

        while f.next and s.next:
            s = s.next
            f = f.next
            if not f.next:
                return False
            
            f = f.next

            if f == s:
                return True
        
        return False