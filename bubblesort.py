def bubbleSort(arr):
    llen = len(arr)-1

    for i in range(llen):
        for j in range(llen-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
llist = [32, 45, 52, 23, 14, 47, 11]
print(bubbleSort(llist))
