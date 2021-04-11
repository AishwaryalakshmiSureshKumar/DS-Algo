def middleelemSum(arr1, arr2, n):
    temp = [0 for x in range(n+n)]
    i, j, k =0, 0, 0
    while(i<n):
        temp[k] = arr1[i]
        i+=1
        k+=1
    while(j<n):
        temp[k]=arr2[j]
        j+=1
        k+=1

    temp.sort()
    print(temp)

    mid = (n*2)//2

    if mid%2==0:
        return temp[mid]+temp[mid+1]
    else:
        return temp[mid]+temp[mid-1]
    

case = int(input())
for i in range(case):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(middleelemSum(arr1, arr2, n))
