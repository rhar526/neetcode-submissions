"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = { None : None }
        curr = start = head

        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = start

        while curr:
            nodes[curr].next = nodes[curr.next]
            nodes[curr].random = nodes[curr.random]
            curr = curr.next
        
        return nodes[start]