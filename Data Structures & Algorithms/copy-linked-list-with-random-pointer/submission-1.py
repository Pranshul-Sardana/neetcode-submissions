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
        #Initiate a dictionary to store all the values
        store_dict = {None: None}

        #First pass: Initiate new with values and Store in the dictionary
        curr = head
        while curr:
            new = Node(curr.val)
            store_dict[curr] = new
            curr = curr.next

        #Second pass: Make connections
        curr = head
        while curr:
            new = store_dict[curr]
            new.next = store_dict[curr.next]
            new.random = store_dict[curr.random]
            curr = curr.next

        #Return
        return store_dict[head]
