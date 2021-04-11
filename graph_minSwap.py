arr = list(map(int, input().split()))
arrS = sorted(arr)
count=0
for i in range(len(arr)):
    if arr[i]!=arrS[i]:
        count+=1
print(arr)
print(arrS)
