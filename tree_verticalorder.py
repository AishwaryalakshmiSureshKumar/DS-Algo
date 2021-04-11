def verticalorderTraversal(root, level, vt):
    global visited
    if root:
        temp = [level, vt, root.data]
        visited.append(temp)
        verticalorderTraversal(root.left, level+1, vt-1)
        verticalorderTraversal(root.right, level+1, vt+1)

def sortt():
    global visited
    for i in range(len(visited)-1):
        for j in range(i+1,len(visited)):
            if(visited[i][1]==visited[j][1] and visited[i][0]>visited[j][0]):
                    visited[i],visited[j]=visited[j],visited[i]    
            elif(visited[i][1]>visited[j][1]):
                visited[i],visited[j]=visited[j],visited[i]

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


root = Node(2)
#root.left = Node(2)
root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
root.right.left = Node(4)
visited = []
verticalorderTraversal(root, 1, 0)
sortt()
for i in visited:
    print(i[2], end=' ')
