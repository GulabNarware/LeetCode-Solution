class MyLinkedList(object):
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head=None
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        count =0
        curr=self.head
        while curr:
            if index ==count:
                return curr.val
            count+=1
            curr=curr.next
        return -1
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node=MyLinkedList.Node(val)
        node.next=self.head
        self.head=node
    
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node=MyLinkedList.Node(val)
        
        if not self.head:
            self.head = node
            return
        curr=self.head

        while curr.next is not None:
            curr=curr.next
        curr.next=node
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return

        node = MyLinkedList.Node(val)
        curr = self.head
        count = 0

        while curr and count < index - 1:
            curr = curr.next
            count += 1

        if not curr:
            return

        node.next = curr.next
        curr.next = node
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0

        while curr and curr.next:
            if count == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            count += 1
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtself.head(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)