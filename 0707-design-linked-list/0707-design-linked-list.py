class MyLinkedList:
    class Node:
        def __init__(self,val):
            self.val=val
            self.next=None


    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        count =0
        curr=self.head
        while curr:
            if count ==index:
                return curr.val
            curr=curr.next
            count+=1
        return -1
    
    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head=MyLinkedList.Node(val)
        else:
            node=MyLinkedList.Node(val)
            curr=node
            curr.next=self.head
            self.head=curr



    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head=MyLinkedList.Node(val)

        else:
            curr=self.head

            while curr.next is not None:
                curr=curr.next

            curr.next=MyLinkedList.Node(val)

    def addAtIndex(self, index: int, val: int) -> None:

        if index==0:
            self.addAtHead(val)
            return 

        node = MyLinkedList.Node(val)
        curr = self.head
        count = 0

        while curr and count < index-1:
            count +=1
            curr=curr.next

        if not curr:
            return 

        node.next=curr.next
        curr.next=node

    def deleteAtIndex(self, index: int) -> None:

        if not self.head:
            return 

        if index==0:
            self.head=self.head.next

        count =0
        curr=self.head

        while curr and curr.next:
            if count ==index-1:
                curr.next=curr.next.next
                return 

            curr=curr.next
            count+=1


            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)