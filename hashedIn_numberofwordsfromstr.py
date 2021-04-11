strr = input()
word = input()
count=0
res=0
word = set(word)
for i in word:
    for j in strr.lower():
        if i==j:
            count+=1
res = count%len(word)
print(res)
    
