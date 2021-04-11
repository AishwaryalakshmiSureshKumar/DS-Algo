'''dictt = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['x','y','z']}

strr=input().split('*')
for i in strr:
    j=i[0]
    llen1=len(i)
    llen2=len(dictt[int(j)])
    num = llen1%llen2
    ch = dictt[int(j)][num-1]
    print(ch.upper(),end='')'''
import random
for i in range(10):
    print(random.randrange(1,7))
