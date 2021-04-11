#strr = int(input())
def palindrome(st, en, strr):
    stack = []
    count = 0
    res =[]
    for i in range(st, en):
        stack.append(strr[i])

    for i in range(st, en):
        if strr[i]!=stack.pop():
            count+=1
        else:
            res.append(strr[i])

    
    return res, count

#strr = 'nayannamantenet'
#strr = 'aaaaa'
strr = 'aaaabaaaa'
n = len(strr)
res = []
if n%3==0:
    l = round(n/3)
    for i in range(0,n,l):
        res, count = palindrome(i, i+l, strr)
        if not count:
            for i in res:
                print(i, end='')
        print()
else:
    for i in range(0, n):
        res, count = palindrome(2, n, strr)
        if not count:
            print(strr[0])
            print(strr[1])
            for i in res:
                print(i, end='')
            break
        print()
            
    
