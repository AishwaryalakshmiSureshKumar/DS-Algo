#code
def actSelection(s, f, n, ind):
    
    time_limit = f[0]
    for i in range(len(ind)):
        if ind[i][0]==s[0]:
            print(ind[i][2], end=' ')
            break
    stack = []
    for i in range(1, n):
        if s[i]>=time_limit:
            stack.append(s[i])
            time_limit = f[i]
    
    for i in range(len(stack)):
        for j in range(len(ind)):
            if ind[j][0]==stack[i]:
                print(ind[j][2], end=' ')
                break
def heapify(s, f, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left<n and f[left]>f[largest]:
        largest = left

    if right<n and f[right]>f[largest]:
        largest = right

    if largest!=i:
        f[i], f[largest] = f[largest], f[i]
        s[i], s[largest] = s[largest], s[i]
        heapify(s, f, n, largest)
        
def sort(s, f):
    n = len(s)
    for i in range((n//2)-1, -1, -1):
        heapify(s, f, n, i)

    for i in range(n-1, -1, -1):
        f[i], f[0] = f[0], f[i]
        s[i], s[0] = s[0], s[i]
        heapify(s, f, i, 0)


case = int(input())
for i in range(case):
    llen = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    index = []
    for i in range(llen):
        index.append([s[i], f[i], i+1])
    sort(s, f)
    print(s)
    print(f)
    actSelection(s, f, llen, index)
    print()
