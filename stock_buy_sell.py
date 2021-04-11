def stock(a,n):
    i=0
    j=1
    result=[]
    flag=0
    while(j<n):
        if(a[j]>=a[j-1]):
            j+=1
            continue
        else:
            if i==(j-1):
                flag=1
            else:
                flag=0
                result.append(i)
                result.append(j-1)
            i=j
        j+=1
    if flag==1:
        print("No Profit")
    else:
        result.append(i)
        result.append(j-1)
        for i in range(0,len(result),2):
            print('('+str(result[i])+' '+str(result[i+1])+')', end=' ')
        print()
    
            

test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    stock(arr, arr_len)
            
            
