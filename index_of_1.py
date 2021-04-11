
def index_of_1(num):
    count=0
    zero = 0
    index=0
    while num>0:
        count+=1
        num=num//10
    print(count)
    while num:
        if num%10==0:
            num=num/10
            zero+=1
        else:
            index = count - zero
    return index

test_case = int(input())
for i in range(test_case):
    num = int(input())
    print(index_of_1(num))
