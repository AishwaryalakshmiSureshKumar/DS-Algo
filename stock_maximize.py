class Stack:
    def __init__(self):
        self.stack = []

    def push(self, dataVal):
        self.stack.append(dataVal)

    def checkemptyStack(self):
        return len(self.stack)==0

    def pop(self):
        return self.stack.pop()
        
        

case = int(input())
for i in range(case):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    s = Stack()
    for i in range(n):
        if s.checkemptyStack() is True:
            s.push(arr[i])
        elif i==n-1:
            if arr[i-1]<arr[i]:
                while s.checkemptyStack() is not True:
                    s.pop()
        else:
            if arr[i-1]<arr[i]:
                s.push(arr[i])
            else:
                while s.checkemptyStack() is not True:
                    s.pop()
                s.push(arr[i])
                    
    if s.checkemptyStack():
        print('0')
    else:
        print('Not Empty')



'''3
3
5 3 2
3
1 2 100
4
1 3 1 2'''
                
    
