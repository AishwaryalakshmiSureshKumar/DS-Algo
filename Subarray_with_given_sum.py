def find(arr,n,k):
    
    for i in range(n):
        flag=0
        a=0
        b=0
        summ=arr[i]
        for j in range(i+1, n):
            summ = summ+arr[j]
            if summ==k:
                a,b = i+1,j+1
                flag =1
                break
        if flag==1:
            break
    if flag==0:
        print('-1')
    else:
        print(a,b)
            
            

t=int(input())
for ii in range(t):
    temp=[int(x) for x in input().split()]
    n,summ=temp[0],temp[1]
    arr=[int(x) for x in input().split()]
    a = find(arr,n,summ)
    #print(a[0], a[1])

'''2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10'''
