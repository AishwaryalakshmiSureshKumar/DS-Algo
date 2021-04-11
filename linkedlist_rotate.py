class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head==None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last=last.next
        last.next=new_node

    def rotate(self, lr):
        prev=self.head
        temp=prev
        curr=self.head
        i=0
        while i<lr:
            prev=curr
            curr=curr.next
            i+=1
        self.head = curr
        prev.next = None
        while(curr.next):
            curr=curr.next
        curr.next=temp
        temp1 = self.head
        while(temp1.next):
            print(temp1.data, end=' ')
            temp1=temp1.next
        print(temp1.data)
    print()
    
test_case = int(input())
for i in range(test_case):
    llen = int(input())
    lis = list(map(int, input().strip().split()))
    lr = int(input())
    llist = LinkedList()
    for i in range(llen):
        llist.push(lis[i])
    llist.rotate(lr)
