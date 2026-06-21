# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index={}
        if not head:
            return None

        curr=head
        indx=-1
        while curr:
            if curr not in index:
                indx+=1
                index[curr]=indx
                curr=curr.next
            else:  

            
                return curr
        return None



       