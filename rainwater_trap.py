
def water_trap(a, l):
    first = a[0]
    sum_water =0
    trap =0
    for i in range(1, l):
        if a[i]<first:
            trap = first - a[i]
            sum_water = sum_water + trap
    return sum_water


test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=list(map(int, input().split()))
    print(water_trap(arr, arr_len))
