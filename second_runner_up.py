n = int(input())
arr = map(int, input().split())
listt = list(set(arr))

listt.sort()
print(listt)
print(listt[len(listt)-2])
