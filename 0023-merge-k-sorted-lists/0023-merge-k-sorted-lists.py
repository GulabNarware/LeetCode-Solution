# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        res=[]
        if len(lists)==0:
            return 

        for i in lists:
            if i is None:
                continue


            while i.next is not None:

                res.append(i.val)
                i=i.next

            res.append( i.val)
        if not res:
            return None
        res.sort()
        head=ListNode(res[0])
        node=head
        for i in range(1,len(res)):

            node.next=ListNode(res[i])
            node=node.next

        return head
            



            
            

