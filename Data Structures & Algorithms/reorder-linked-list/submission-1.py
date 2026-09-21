# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Get the second half of the Linkedlist
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse it
        curr = slow.next
        rev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp

        #Merge the first and second halves
        first, second = head, rev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second #.next
            second.next = temp1
            first, second = temp1, temp2
            