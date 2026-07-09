# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = 0

        c1, c2 = l1, l2

        while c1 and c2:
            summ = c1.val + c2.val + carry
            rem = summ%10
            carry = 1 if summ - rem != 0 else 0
            node.next = ListNode(rem)
            node = node.next
            c1, c2 = c1.next, c2.next
        
        if not c1 and not c2 and carry == 1:
            node.next = ListNode(carry)
        else:
            while c1 or c2:
                if c1:
                    sum1 = c1.val + carry
                    rem1 = sum1%10
                    carry = 1 if sum1 - rem1 != 0 else 0
                    node.next = ListNode(rem1)
                    node = node.next
                    c1 = c1.next

                if c2:
                    sum2 = c2.val + carry
                    rem2 = sum2%10
                    carry = 1 if sum2 - rem2 != 0 else 0
                    node.next = ListNode(rem2)
                    node = node.next
                    c2 = c2.next

                if not c1 and not c2 and carry == 1:
                    node.next = ListNode(carry)
        return dummy.next
                
