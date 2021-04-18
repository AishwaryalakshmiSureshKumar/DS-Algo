list1 = []
new_list = []
for _ in range(int(input())):
    list2 = []
    name = input()
    score = float(input())
    new_list.append(score)
    list2.append(name)
    list2.append(score)
    list1.append(list2)

new_list.sort()
new_list = list(set(new_list))
new_list.sort()
print(new_list)
val = new_list[1]
result = []
for i in range(len(list1)):
    if list1[i][1]==val:
        result.append(list1[i][0])
result.sort()
for i in result:
    print(i)


