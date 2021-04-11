class Stack():
    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack) == 0

    def push(self, dataVal):
        return self.stack.append(dataVal)

    def pop(self):
        return self.stack.pop()


test_case = int(input())
for i in range(test_case):
    str1 = input()
    AStack = Stack()
    k=len(str1)-1
    while k>-1:
        if str1[k]=='.':
            while AStack.check_empty() is not True:
                print(AStack.pop(), end='')
            print('.', end='')
        else:
            AStack.push(str1[k])
        k-=1
    while AStack.check_empty() is not True:
        print(AStack.pop(), end='')
    print()
            
