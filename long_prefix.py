#code

def commonPrefix(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    result = ""

    i,j=0,0
    while i<=n1-1 and j<=n2-1:
        if s1[i]!=s2[j]:
            break
        result+=s1[i]
        i+=1
        j+=1
    if result:
        return result
    else:
        return -1


def prefix(s, l):
    
    if l==1:
        print(s)
    else:
        s.sort(reverse=False)
        print(commonPrefix(s[0], s[l-1]))
    


t=int(input())
for cases in range(t):
    length = int(input())
    if length==1:
        string=input()
    else:
        string=list(map(str, input().split(' ')))
    prefix(string, length)
