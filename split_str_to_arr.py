s="[[1,0,1,0],[1,0,1,1]]"
arr=[]
temp=[]
count=0
for i in s:
    try:
        i = int(i)
        count+=1
        temp.append(i)
        if count==3:
            arr.append(temp)
            temp=[]
            count=0
    except ValueError:
        pass


