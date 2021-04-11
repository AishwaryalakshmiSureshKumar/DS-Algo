def find(arr, k):
    for i in range(len(arr)):
        if arr[i][1] == k:
            return i
    return -1

def bottomView(root, level, vt):

    global visited
    if root:
        index = find(visited, vt)
        if index>=0:
            if visited[index][0]<=level:
                visited[index][0] = level
                visited[index][2] = root.data

        else:
            temp = [level, vt, root.data]
            visited.append(temp)

        bottomView(root.left, level+1, vt-1)
        bottomView(root.right, level+1, vt+1)
        

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

'''test_case = int(input())
for i in range(test_case):
    elem_list = list(map(int, input().split()))
    root = Node(elem_list[0])
    for i in range(1, len(elem_list)):
        root.insert(elem_list[i])'''
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(40)
root.right.left = Node(60)

visited = []
bottomView(root, 1, 0)
for i in visited:
    print(i[2], end=' ')
