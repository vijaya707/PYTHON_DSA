class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
class singlelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insertingstart(self,value):
        Newnode=Node(value)
        if self.head is None:
            self.head=Newnode
            self.head=self.tail=Newnode;self.size +=1;
        return
        Newnode.next=self.head
        
            





