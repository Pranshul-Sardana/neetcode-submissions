# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Initiate a empty and dummy node
        dummy = ListNode()
        combined = dummy

        #While any of the lists
            #If val1<=val2, add list1. Move the list forward
            #else add list2. Move the list forward
            #Move the dummy
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        #If either of the lists is non-empty, add them to the dummy
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2

        #Return combined
        return combined.next

