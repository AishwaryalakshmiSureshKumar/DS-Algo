
def LeftView(root, level, maxlevel):

    if root is None:
        return 0
    else:
        if maxlevel[0]<level:
            print(root.data, end=' ')
            maxlevel[0] = level

        LeftView(root.left, level+1, maxlevel)
        LeftView(root.right, level+1, maxlevel)

def printLeft(root):

    maxlevel = [0]

    LeftView(root, 1, maxlevel)
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val]  + inorder(root.right)
        
        
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

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

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
        


'''test_case = int(input())
for i in range(test_case):
    elem_list = list(map(int, input().split()))
    root = Node(elem_list[0])
    for i in range(1,len(elem_list)):
        root.insert(elem_list[i])
    printLeft(root)'''

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)
#printLeft(root)
ans = inorder(root)
print(ans)
