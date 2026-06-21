# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self,head,n):
        # """
        # :type head: Optional[ListNode]
        # :type n: int
        # :rtype: Optional[ListNode]
        # """

        count =0
        curr=head

        while curr:
            count +=1
            curr=curr.next

        if count==n:
            head=head.next
            return head

        total =count-n
        c=0
        new=head
        while c< (total-1):
            c+=1
            
            new=new.next

        new.next=new.next.next

        return head
            

        