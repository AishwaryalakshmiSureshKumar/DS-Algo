class Queue:
    def __init__(self):
        self.s1 =[]
        self.s2 =[]

    def enqueue(self, dataVal):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(dataVal)

        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1)==0:
            print('-1', end=' ')
        else:
            x=self.s1[-1]
            self.s1.pop()
            print(x, end=' ')



test_case = int(input())
for i in range(test_case):
    tests = int(input())
    arr=list(map(int, input().split()))
    TheQueue = Queue()
    i=0
    while i<len(arr):
        if arr[i]==1:
            TheQueue.enqueue(arr[i+1])
            i+=2
        elif arr[i]==2:
            TheQueue.dequeue()
            i+=1
    
            
