class Stack:

    def __init__(self):
        self.stack = []

    def push(self, dataVal):
        self.stack.append(dataVal)

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        print('-1', end=' ')

    def getMin(self):
        if len(self.stack)==0:
            print('-1', end=' ')
        else:
            print(min(self.stack), end=' ')
            

test_case = int(input())
for i in range(test_case):
    num = int(input())
    arr=list(map(int, input().strip().split()))
    AStack = Stack()
    while i<len(arr):
        if arr[i]==1:
            AStack.push(arr[i+1])
            i+=2
        elif arr[i]==2:
            print(AStack.pop(), end=' ')
            i+=1
        elif arr[i]==3:
            AStack.getMin()
            i+=1
            
            
            
            
