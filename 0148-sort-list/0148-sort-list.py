# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # if not head:
        #     return head

        # count=0
        # c=head
        # while c is not None:
        #     c=c.next
        #     count+=1
        # while count>0:
        #     temp2=head
            
        #     while temp2.next is not None:
        #         if temp2.val > temp2.next.val:
        #             temp2.val,temp2.next.val=temp2.next.val,temp2.val
                    
        #         temp2=temp2.next


        #     count-=1

        # return head
        
        if not head:
            return head
        temp=head
        arr=[]

        while temp:
            arr.append(temp.val)

            temp=temp.next

        arr.sort()

        head=ListNode(arr[0])
        temp2=head
        for i in range(1,len(arr)):
            temp2.next=ListNode(arr[i])
            temp2=temp2.next

        return head

