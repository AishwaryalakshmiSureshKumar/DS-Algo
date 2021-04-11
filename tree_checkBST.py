flag = 1
def checkBST(root):
    global flag
    if root is None:
        return True
    else:
        if((root.left) and (root.right) and (root.data<root.left.data or root.data>root.right.data)):
            flag = 0
        checkBST(root.left)
        checkBST(root.right)
        if flag:
            return True
        else:
            return False
    

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

    def inorder(self):
        if (not root):
            return
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

test_case = int(input())
for i in range(test_case):
    elem_list = list(map(int, input().split()))
    root = Node(elem_list[0])
    i=1
    while i<len(elem_list):
        root.insert(elem_list[i])
    if checkBST(root):
        print('1')
    else:
        print('0')
