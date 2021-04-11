#code
def toggleBits(n, l, r):
    
    i=1
    strr = ''
    num=0
    
    while(n>0):
        rem=n%2
        if i>=l and i<=r:
            if rem==0:
                strr+='1'
            else:
                strr+='0'
        else:
            strr+=str(rem)
        i+=1
        n//=2
    strr = strr[::-1]
    print(int(strr, 2))

case = int(input())
for i in range(case):
    n, l, r = list(map(int, input().split()))
    toggleBits(n, l, r)
