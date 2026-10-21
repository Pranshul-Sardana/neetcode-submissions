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
        retDict = {None: None}

        #Copy values first to craete a base structure
        curr = head
        while curr:
            temp = Node(curr.val)
            retDict[curr] = temp
            curr = curr.next
            
        
        #Copy connections
        curr = head
        while curr:
            temp = retDict[curr]
            temp.next = retDict[curr.next]
            temp.random = retDict[curr.random]
            curr = curr.next
            
        return retDict[head]