
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head==None:
            print('-1', end=' ')
            return
        
        temp=self.head

        print(temp.data, end=' ')
        self.head = temp.next
        temp = self.head


test_case = int(input())
for i in range(test_case):
    llen = int(input())
    llis = list(map(int, input().split()))
    llist = LinkedList()
    i=0
    while i<len(llis):
        if llis[i]==1:
            llist.push(llis[i+1])
            i+=2
        elif llis[i]==2:
            llist.pop()
            i+=1
    print()
