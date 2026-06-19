# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return 

        prev=head

        


        if head.next==None:
            return head

        curr=head.next
        prev=head

        while prev and curr :
            prev.val,curr.val=curr.val,prev.val

            if prev.next.next is not None:
                prev=prev.next.next
            else:
                return head

            if curr.next.next is not None:
                curr=curr.next.next

            else:
                return head

        return head



        return head
        