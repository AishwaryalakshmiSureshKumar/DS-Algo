
def rem_duplicate(s, l):
    dup = []
    for i in range(l):
        if strr[i] not in dup:
            dup.append(strr[i])
        else:
            continue
    return dup


test_case = int(input())
for i in range(test_case):
    strr = input()
    l = len(strr)
    res = rem_duplicate(list(strr), l)
    for i in res:
        print(i, end='')
    print()
