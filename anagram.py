
class pySolution:

    def anagram(self, arr):
        i=0
        count=0
        s1 = arr[0]
        s2 = arr[1]
        while len(s1)==len(s2) and i<len(s1):
            if s1[i] in s2:
                count+=1
            i+=1
        if count==len(s1):
            return 'YES'
        else:
            return 'NO'

test_case = int(input())
for i in range(test_case):
    arr=list(map(str, input().split(' ')))
    print(pySolution().anagram(arr))
