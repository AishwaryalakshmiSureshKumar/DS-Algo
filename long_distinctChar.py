NO_OF_CHARS =256
def distinct_char(s):

    last_index = [-1]*NO_OF_CHARS

    n=len(s)
    res=0
    i=0

    for j in range(0,n):

        i = max(i, last_index[ord(s[j])]+1)

        res = max(res, j-i+1)

        last_index[ord(s[j])] = j

    print(res)

        


t = int(input())
for i in range(t):
    string= input()
    distinct_char(string)
