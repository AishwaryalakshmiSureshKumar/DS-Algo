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
            last = last.next
        last.next=new_node

    def pop(self):

        if self.head==None:
            print('-1', end=' ')
            return
        
        ptr = self.head

        if ptr.next is not None:
            print(ptr.data, end=' ')
            self.head = ptr.next
            ptr = self.head
        else:
            print(ptr.data, end=' ')
            ptr = self.head = None

    def isEmpty(self):
        return self.head == None


test_case = int(input())
for i in range(test_case):
    llen = int(input())
    lis = list(map(int, input().split()))
    llist = LinkedList()
    i=0
    while i < len(lis):
        if lis[i]==1:
            llist.push(lis[i+1])
            i+=2
        elif lis[i]==2:
            llist.pop()
            i+=1
    print()
