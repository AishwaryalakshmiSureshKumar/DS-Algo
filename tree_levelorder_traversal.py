def levelOrderTraversal(root, level, vt):
    global visited
    if root:
        temp = [level, vt, root.data]
        visited.append(temp)

        levelOrderTraversal(root.left, level+1, vt-1)
        levelOrderTraversal(root.right, level+1, vt+1)

def sortt():
    global visited

    for i in range(len(visited)-1):
        for j in range(i+1, len(visited)):
            if visited[i][0]==visited[j][0] and visited[i][1]>visited[j][1]:
                visited[i], visited[j] = visited[j], visited[i]
            elif visited[i][0]>visited[j][0]:
                visited[i], visited[j] = visited[j], visited[i]

class Tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


root = Tree(10)
root.left = Tree(20)
root.left.left = Tree(30)
root.left.right = Tree(40)
root.right = Tree(50)
root.right.left = Tree(60)
root.right.right = Tree(70)
visited = []
levelOrderTraversal(root, 1, 0)
sortt()
for i in visited:
    print(i[2], end=' ')
