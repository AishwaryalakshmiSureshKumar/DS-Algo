
def str_rotate(s1, s2, n1, n2):
    if n1!=n2:
        return 0
    clock_rot =""
    anti_clock_rot =""

    anti_clock_rot = (anti_clock_rot + s2[n2-2:] + s2[0:n2-2])
    clock_rot = (clock_rot + s1[0:2] + s1[2:])

    return (s1==anti_clock_rot or s1==clock_rot)

    
    


t = int(input())
for i in range(t):
    str1= input()
    print()
    str2= input()
    len1 = len(str1)
    len2 = len(str2)
    res = str_rotate(str1, str2, len1, len2)
    if res:
        print(1)
    else:
        print(0)
