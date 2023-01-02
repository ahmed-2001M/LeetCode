# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        start = head
        while head:
            l+=1
            head = head.next
        l = l//2
        while l :
            l-=1
            start = start.next
        return start
            