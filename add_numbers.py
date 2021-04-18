class Node:
    def __init__(self, data):
        self.val = data
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
            last = last.next
        last.next = new_node

    def add(self, l1, l2):
        temp = None
        prev = Node(None)
        carry = 0
        
        while(l1 is not None or l2 is not None):
            
            first = 0 if l1 is None else l1.val
            second = 0 if l2 is None else l2.val
            
            summ = carry + first + second
            
            carry = 1 if summ>=10 else 0
            
            summ = summ if summ<10 else summ%10
            
            temp = Node(summ)
            
            if self.head is None:
                self.head = temp
                prev = temp
            else:
                prev.next = temp
                prev = temp

            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        if carry>0:
            temp.next = Node(carry)
            
        temp=temp.next
        prev.next = temp
        temp.next = None

        t=self.head
        while t:
            print(t.val)
            t=t.next
        

        


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

list1 = LinkedList()
list2 = LinkedList()

for i in l1:
    list1.push(i)
for i in l2:
    list2.push(i)

res = LinkedList()
res.add(list1.head, list2.head)

