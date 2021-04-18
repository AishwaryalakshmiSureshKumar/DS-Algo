def fun(b, e, l):
    if e not in l:
        return 0
    else:
        res = 0
        l.insert(0,b)
        for i in range(len(l)-1):
            
            count = [0]*256
            

            for m in l[i]:
                
                if m in l[i+1]:
                    print(m)
                    count[ord(str(m))]+=1
            n = len(l[i])
            p = len(l[i+1])
            if n==1 and p==1 and l[i]!=l[i+1]:
                res+=1
            elif sum(count)==len(l[i])-1:
                res+=1
            else:
                continue
        return res
            
                
        

    

beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]

print(fun(beginWord, endWord, wordList))
