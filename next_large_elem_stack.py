class Stack:
    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack)==0

    def push(self, dataVal):
        self.stack.append(dataVal)

    def top(self):
        return self.stack[0]

    def pop(self):
        return self.stack.pop()



test_case = int(input())
for i in range(test_case):
    length = int(input())
    arr = list(map(int, input().split()))
    AStack = Stack()
    for i in range(length):
        if AStack.check_empty():
            AStack.push(arr[i])
            for j in range(i+1, length):
                if AStack.top()<arr[j]:
                    print(arr[j], end=' ')
                    flag=1
                    while AStack.check_empty() is not True:
                        AStack.pop()
                    break
                else:
                    AStack.push(arr[j])
            
        if flag:
            flag=0
        else:
            print('-1', end=' ')
            
            
