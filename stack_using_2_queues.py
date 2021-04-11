class Stack:
    def __init__(self):
        self.q1 = list()
        self.q2 = list()
        self.curr_size = 0

    def push(self, dataVal):

        self.curr_size +=1

        self.q2.insert(0, dataVal)
        
        while len(self.q1)!=0:
            self.q2.insert(0,self.q1[0])
            self.q1.pop()
        
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):

        if len(self.q1)==0:
            print('-1',end=' ')
        else:
            x = self.q1.pop()
            print(x, end=' ')
            self.curr_size-=1
            

test_case = int(input())
for i in range(test_case):
    num = int(input())
    arr = list(map(int, input().strip().split()))
    AStack = Stack()
    while i<len(arr):
        if arr[i]==1:
            AStack.push(arr[i+1])
            i+=2
        elif arr[i]==2:
            AStack.pop()
            i+=1
    print()
