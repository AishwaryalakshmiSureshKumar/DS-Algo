def find(n,s):
    result = 0
    res = int(str(9)*n)
    summ=0
    while res!=0:
        summ+=res%10
        res//=10
    if summ<s or s==0:
        return '-1'
    else:
        for i in range(n-1,-1,-1):
                if(s>=9):
                    result+=9*(10**i)
                    s-=9
                elif(s in range(1,9)):
                    result+=s*(10**i)
                    s=0
        return result

t=int(input())
for i in range(t):
    temp=[int(x) for x in input().split()]
    n,s=temp[0],temp[1]
    print(find(n,s))
