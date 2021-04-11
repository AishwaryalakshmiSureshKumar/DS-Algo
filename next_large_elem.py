
def max_arr(a, n, i, j):
    flag=0
    while j<n:
        if a[i]<a[j]:
            max_el.append(a[j])
            flag=1
            break
        
        j+=1
    if flag:
        return max_el
    else:
        return max_el.append('-1')


def next_large_elem(a, n):
    i=0
    j=1
    while i<n:
        max_arr(a, n, i, j)
        i+=1
        j=i+1
    return max_el
    

test_case = int(input())
for i in range(test_case):
    length = int(input())
    arr = list(map(int, input().split()))
    max_el = []
    result = next_large_elem(arr, length)
    for i in result:
        print(i, end=' ')
    print()
        
