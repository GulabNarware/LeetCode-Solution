# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        last=head
        temp=[]

        while last:
            temp.append(last.val)
            last=last.next


        curr =head

        for i in range(len(temp)-1,-1,-1):

            curr.val=temp[i]
            curr=curr.next


        return head