class Stack:

    def __init__(self):
        self.stack = []

    def push(self, dataVal):
        return self.stack.append(dataVal)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def check_empty(self):
        return len(self.stack)==0



test_case = int(input())
for i in range(test_case):
    par = str(input())
    AStack = Stack()
    res =0
    for i in par:
        if(i=='(' or i=='[' or i=='{'):
            AStack.push(i)
        elif AStack.check_empty() is not True:
            if i==')' and AStack.peek()=='(':
                AStack.pop()
            elif i==']' and AStack.peek()=='[':
                AStack.pop()
            elif(i=='}' and AStack.peek()=='{'):
                AStack.pop()
            else:
                res=0
                break
        else:
            res=0
            break
    if AStack.check_empty():
        res=1
    else:
        res=0

    if res:
        print("balanced")
    else:
        print("not balanced")
