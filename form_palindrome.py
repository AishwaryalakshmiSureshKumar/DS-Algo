import sys


def findMinInsertion(s, l, h):

    if l>h:
        return sys.maxsize
    if l==h:
        return 0
    if l==h-1:
        return 0 if(s[l]==s[h]) else 1

    if (s[l]==s[h]):
        return findMinInsertion(s, l+1, h-1)
    else:
        return (min(findMinInsertion(s, l, h-1),findMinInsertion(s, l+1, h))+1)


test_case = int(input())
for i in range(test_case):
    string = input()
    print(findMinInsertion(string, 0, len(string)-1))
    
