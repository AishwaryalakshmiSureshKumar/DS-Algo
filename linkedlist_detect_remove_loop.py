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

    def loopHere(self, pos):
        if pos==0:
            return
        
        walk = self.head

        for i in range(1, pos):
            walk = walk.next

        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next =walk

    def isLoop(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while slow_ptr!=fast_ptr:
            if fast_ptr is None or fast_ptr.next is None:
                return False
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return slow_ptr

    def isPrint(self):
        temp=self.head
        while(temp.next):
            print(temp.data, end=' ')
            temp = temp.next
        print(temp.data, end=' ')

    def removeLoop(self, ptr):
        ptr1=self.head
        
        while(1):
            ptr2 = ptr
            while(ptr2.next!=ptr and ptr2.next!=ptr1):
                ptr2 = ptr2.next

            if ptr2.next==ptr1:
                break
                
            ptr1=ptr1.next

        ptr2.next = None


test_case = int(input())
for i in range(test_case):
    llen = int(input())
    lis = list(map(int, input().strip().split()))
    ldr = int(input())
    llist = LinkedList()
    for i in range(llen):
        llist.push(lis[i])
    llist.loopHere(ldr)
    result = llist.isLoop()
    if result:
        llist.removeLoop(result)
    else:
        print("No Loop")
    llist.isPrint()
    
