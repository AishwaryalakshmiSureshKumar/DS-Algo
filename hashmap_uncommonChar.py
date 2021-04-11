#code
def uncommonChar(str1, str2):
    ll = []
    for i in str1:
        if i not in str2 and i not in ll:
            ll.append(i)
            
    for i in str2:
        if i not in str1 and i not in ll:
            ll.append(i)
    ll = sorted(ll)
    for i in ll:
        print(i,end='')


    '''MAX_CHAR = 26
    def uncommonChar(str1, str2):
        result = [0]*MAX_CHAR
        
        for i in range(0, MAX_CHAR):
            result[i] = 0
            
        l1 = len(str1)
        l2 = len(str2)
        
        for i in range(l1):
            
            result[ord(str1[i])-ord('a')]=1
            
        for i in range(l2):
            if result[ord(str2[i])-ord('a')]==1 or result[ord(str2[i])-ord('a')]==-1:
                result[ord(str2[i])-ord('a')]=-1
            else:
                result[ord(str2[i])-ord('a')]=2
        for i in range(0, MAX_CHAR):
            if result[i]==1 or result[i]==2:
                print(chr(i + ord('a')), end=' ')'''


case = int(input())
for i in range(case):
    str1 = str(input())
    str2 = str(input())
    uncommonChar(str1, str2)
