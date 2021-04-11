class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        '''new_node.next = self.head
        self.head = new_node'''
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def reverse(self):
        prev=None
        curr = self.head
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        temp=self.head
        while temp:
            print(temp.data, end=' ')
            temp=temp.next


test_case = int(input())
for i in range(test_case):
    llen = int(input())
    lis = list(map(int, input().split()))
    llist = LinkedList()
    for i in range(llen):
        llist.push(lis[i])
    llist.reverse()
