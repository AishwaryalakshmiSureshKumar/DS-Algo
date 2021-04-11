def pairSwap(head):
    temp = head

    if temp is None:
        return

    while(temp is not None and temp.next is not None):

        temp.data, temp.next.data = temp.next.data, temp.data

        temp = temp.next.next

    return head
    
def printList(n):

    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()


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
        while last.next:
            last=last.next
        last.next=new_node



test_case = int(input())
for i in range(test_case):
    llen = int(input())
    llis = list(map(int, input().strip().split()))
    llist = LinkedList()
    for i in llis:
        llist.push(i)
    printList(pairSwap(llist.head))
