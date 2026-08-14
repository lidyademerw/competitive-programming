class MyNode:
    def __init__(self, val):
        self.val=val
        self.next=None
        self.prev=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
       

    def get(self, index: int) -> int:
        current=self.head
        position=0
        while current is not None:
            if position==index:
                return current.val
            current=current.next
            position+=1
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = MyNode(val)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head.prev= new_node
            self.head=new_node
    
    def addAtTail(self, val: int) -> None:
        new_node = MyNode(val)
        current=self.head
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node


    def addAtIndex(self, index: int, val: int) -> None:
        if index<=0:
            self.addAtHead(val)
            return
        current=self.head
        position=0
        while current is not None and position < index:
            current=current.next
            position+=1
        if position == index:
            if current is None:
                self.addAtTail(val)
            else:
                new_node = MyNode(val)
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return 
        else:
            position=0
            current=self.head
            if index<0:
                return 
            if index == 0:
                self.head = self.head.next   
                if self.head is not None:  
                    self.head.prev = None
                else:                         
                    self.tail = None      
                return            
            while current is not None and position < index:
                position+=1
                current=current.next
            if current is None:
                return
            if current.next is None:
                self.tail = current.prev      
                self.tail.next = None           
                return 
            
            current.prev.next=current.next
            current.next.prev=current.prev


       
       



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)