def sortedMerge(head1, head2):
    temp = Node(None)
    result = temp

    if head1 is None:
        return head2

    if head2 is None:
        return head1
        
    while(head1 is not None and head2 is not None):
        if head1.data<=head2.data:
            result.next = head1
            head1 = head1.next
        else:
            result.next = head2
            head2 = head2.next
        result = result.next
        
        

    if head1 is None:
        result.next = head2
    elif head2 is None:
        result.next = head1

    return temp.next

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
        while(last.next):
            last = last.next
        last.next = new_node


test_case = int(input())
for i in range(test_case):
    n,m=list(map(int, input().strip().split()))
    a= LinkedList()
    b= LinkedList()
    value1 = list(map(int, input().strip().split()))
    value2 = list(map(int, input().strip().split()))

    for x in value1:
        a.push(x)

    for x in value2:
        b.push(x)

    printList(sortedMerge(a.head,b.head))
