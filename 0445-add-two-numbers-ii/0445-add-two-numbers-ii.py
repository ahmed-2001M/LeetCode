# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(x):
            prev = None
            while x :
                nx = x.next
                x.next = prev
                prev = x
                x = nx
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)

        carry = 0
        res = ListNode()
        ans = res
        
        while l1 or l2 or carry:
            print(res.val)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            carry = val//10
            val = val%10
            res.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            res = res.next
            
        return reverse(ans.next)
            

            

