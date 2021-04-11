def isPalindrome(head):
    temp=head
    stack=[]
    
    while(temp):
        stack.append(temp.data)
        temp=temp.next
        
    temp=head

    while(temp):
        popped = stack.pop()
        if temp.data == popped:
            temp=temp.next
        else:
            return 0
    return 1



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
    lis = list(map(int, input().split()))
    llist = LinkedList()
    for i in lis:
        llist.push(i)
    print(isPalindrome(llist.head))
    
