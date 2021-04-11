class Stack:
    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack)==0

    def peek(self):
        return self.stack[-1]
    
    def push(self, dataVal):
        self.stack.append(dataVal)

    def pop(self):
        return self.stack.pop()
    
            

test_case = int(input())
for i in range(test_case):
    ll = int(input())
    arr=list(map(int,input().split()))

    AStack = Stack()
    max_sum = 0
    sum_arr = []
    for i in range(ll):
        if AStack.check_empty():
            AStack.push(arr[i])
            max_sum = max_sum + arr[i]
        else:
            if AStack.peek()<arr[i]:
                AStack.push(arr[i])
                max_sum = max_sum + arr[i]
            else:
                sum_arr.append(max_sum)
                pop_elem = AStack.pop()
                AStack.push(arr[i])
                max_sum = max_sum + arr[i] - pop_elem
    sum_arr.append(max_sum)
    sum_arr.sort()
    print(sum_arr[-1])

'''1
7
1 101 2 3 100 4 5'''
             
