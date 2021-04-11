def sortedMerge(left, right):
    temp=None
    if left==None:
        return right
    if right==None:
        return left
    if left.data<=right.data:
        temp = left
        temp.next = sortedMerge(left.next, right)
    else:
        temp=right
        temp.next = sortedMerge(left, right.next)
    return temp

def getMiddle(head):
    if head==None:
        return head

    slow_ptr = head
    fast_ptr = head

    while(fast_ptr is not None and fast_ptr.next is not None):
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    return slow_ptr


def mergesort(head):

    if head==None and head.next==None:
        return head

    temp=getMiddle(head)
    nexttoMiddle = temp.next

    temp.next = None

    left = mergesort(head)
    right = mergesort(nexttoMiddle)

    sortedlist = sortedMerge(left, right)
    return sortedlist

def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n=n.next
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
        if self.head == None:
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
    printList(mergesort(llist.head))
