#code
def equalArray(arr1, arr2, n):
    lst = arr2
    count = 0
    for i in arr1:
        if i in lst:
            count+=1
            lst.remove(i)
    if count==n:
        print('1')
    else:
        print('0')



case = int(input())
for i in range(case):
    llen = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    equalArray(list1, list2, llen)
