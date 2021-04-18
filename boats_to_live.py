people = [3,5,3,4]
limit = 5

boat=0
for i in range(len(people)-1):
    visited = [0]*len(people)
    for j in range(len(people)):
        if people[i]==limit:
            boat+=1
            visited[i]=True
            break
        else:
            if people[i]+people[j]==limit and people[j]==False:
                boat+=1
                visited[i]=True
                visited[j]=True
            else:
                boat+=1
                visited[i]=True
print(boat)
