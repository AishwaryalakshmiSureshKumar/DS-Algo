def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n=n.next
    print()

def deleteNode(curr_node):
    next_node = curr_node.next
    curr_node.data = next_node.data
    curr_node.next = next_node.next

    
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
            self.head= new_node
            return
        last = new_node
        while(last.next):
            last = last.next
        last.next = new_node

    def getNode(self, elem):
        temp = self.head
        while (temp.next is not None and temp.data!=elem):
            temp=temp.next
        if temp.data==elem:
            return temp


test_case = int(input())
for i in range(test_case):
    llen = int(input())
    lis = list(map(int, input().strip().split()))
    llist = LinkedList()
    for i in lis:
        llist.push(i)
    delete_elem = int(input())
    to_delete = llist.getNode(delete_elem)
    deleteNode(to_delete)
    printList(llist.head)
