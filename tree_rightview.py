def RightView(root, level, maxlevel):

    if root is None:
        return 0
    else:
        if level>maxlevel[0]:
            print(root.data, end=' ')
            maxlevel[0]=level
            
        RightView(root.right, level+1, maxlevel)   
        RightView(root.left, level+1, maxlevel)
        


def printRight(root):

    maxlevel = [0]

    RightView(root, 1, maxlevel)

class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.right.left = Tree(40)
root.right.right = Tree(60)
printRight(root)
