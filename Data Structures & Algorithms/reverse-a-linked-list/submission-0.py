# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#node has a value and a pointer to the next node
#we loop through the head node going to the next one until we reach null
#we have a reverse node
#and at each node we store it in a new node
#and point the new node to reverse
#so reverse is 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        while head != None:
            orgNext = head.next
            current = head
            current.next = reverse
            reverse = current


            head = orgNext
        return reverse



        