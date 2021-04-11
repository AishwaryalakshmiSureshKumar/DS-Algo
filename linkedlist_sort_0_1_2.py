def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n=n.next
    print()

def sortedList(head):
    
    ptr = head
    count= [0, 0, 0]

    while ptr!=None:
        count[ptr.data]+=1
        ptr = ptr.next

    ptr = head

    i=0
    while ptr!=None:
        if count[i]==0:
            i+=1
        else:
            ptr.data = i
            count[i]-=1
            ptr=ptr.next


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
        last.next = new_node


test_case = int(input())
for i in range(test_case):
    llen = int(input())
    lis = list(map(int, input().split()))
    llist = LinkedList()
    for i in lis:
        llist.push(i)
    sortedList(llist.head)
    printList(llist.head)
    
