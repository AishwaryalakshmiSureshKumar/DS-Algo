def getIntersectPoint(head1, head2):
        curr1 = head1
        curr2 = head2
        while(curr1!=curr2):
            if curr1==None:
                curr1=head2
            else:
                curr1 = curr1.next
            if curr2==None:
                curr2=head1
            else:
                curr2 = curr2.next
        return curr1.data


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        if self.head==None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def head_ret(self):
        return self.head

    def head_chng(self, pos):
        temp=self.head
        for i in range(pos):
            temp=temp.next
        return temp

    def PrintList(self):
        temp = self.head
        while(temp.next):
            print(temp.data, end=' ')
            temp= temp.next
        print(temp)
        


test_case = int(input())
for i in range(test_case):
    llen = list(map(int, input().strip().split()))
    llist1 = LinkedList()
    llist2 = LinkedList()
    nodes_a = list(map(int, input().strip().split()))
    nodes_b = list(map(int, input().strip().split()))
    nodes_common = list(map(int, input().strip().split()))

    for x in nodes_a:
        node = Node(x)
        llist1.push(node)

    for x in nodes_b:
        node = Node(x)
        llist2.push(node)

    for i in range(len(nodes_common)):
        node = Node(nodes_common[i])
        llist1.push(node)
        if i==0:
            llist2.push(node)

    head1 = llist1.head_ret()
    head2 = llist2.head_ret()

    if llen[0]>llen[1]:
        count = llen[0]-llen[1]
        head1 = llist1.head_chng(count)
    elif llen[0]<llen[1]:
        count = llen[1]-llen[0]
        head2 = llist2.head_chng(count)

    print(getIntersectPoint(head1, head2))
    #print(llist1.PrintList())
    #print(llist2.PrintList())
