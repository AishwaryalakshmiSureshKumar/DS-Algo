def heapify(arr, n, i):
    largest = i
    l =2*i+1
    r = 2*i+2

    if l<n and arr[largest]<arr[l]:
        largest = l
    if r<n and arr[largest]<arr[r]:
        largest = r
    if largest!=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def buildHeap(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)



#case = int(input())
case=1
for i in range(case):
    #arr = list(map(int, input().split()))
    arr=[2,3,1,5,4]
    buildHeap(arr)
    print(arr)
               
