def reverse(sa, i, j):
    while i<=j:
        temp=sa[i]
        sa[i]=sa[j]
        sa[j]=temp
        i+=1
        j-=1
    return sa

def reverse_arr(a, n):
    i,j=0,0
    k=n[1]
    while(j+k-1<n[0]):
        reverse(a,i,j+k-1)
        j+=k
        i=j
    if(n[0]%k):
        reverse(a,i,n[0]-1)
    return a


test_case = int(input())
for i in range(test_case):
    arr_len=list(map(int, input().split()))
    arr=list(map(int, input().split()))
    reverse_arr = reverse_arr(arr, arr_len)
    for i in reverse_arr:
        print(i, end=' ')
    print()
