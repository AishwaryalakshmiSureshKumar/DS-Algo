class Node:
    def __init__(self, dataVal):
        self.data = dataVal
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        new_node = Node(newdata)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        '''new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node'''

    def findMid(self, n):
        temp = self.head
        i=0
            
        while i<n:
            temp = temp.next
            i+=1

        return temp.data

    '''def findMid(self):
        fastPtr = self.head.next
        slowPtr = self.head

        while(fastPtr is not None and fastPtr.next is not None):
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
        return slowPtr.data'''
        


test_case = int(input())
for i in range(test_case):
    len_list = int(input())
    list_ = list(map(int, input().split()))
    list1 = Linkedlist()
    for i in range(len_list):
        list1.push(list_[i])
    print(list1.findMid(len_list))
    #print(list1.findMid())
