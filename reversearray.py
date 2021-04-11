arr = [1,4,5,7,6,3]
#print(arr[::-1])
#arr.reverse()
#print(arr)
'''stack = []
for i in arr:
    stack.append(i)
for i in range(len(stack)):
    print(stack.pop(),end=' ')
for i in range(len(arr)-1,-1,-1):
    print(arr[i], end=' ')'''
n=len(arr)
i=0
j=n-1
if n%2==0:
    n=n//2
else:
    n=n//2-1
for k in range(n):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
print(arr)
