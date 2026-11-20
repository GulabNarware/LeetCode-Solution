# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1=0
        num2=0
        while l1 is not None:
            num1=num1*10 + l1.val

            l1=l1.next

        while l2 is not None:
            num2=num2*10 + l2.val

            l2=l2.next

        result=num1+num2
        result=str(result)
 
        l3=ListNode()
        head=l3

        for i in result:
            node=ListNode(int(i))
            l3.next=node
            l3=l3.next
        return head.next




        
        