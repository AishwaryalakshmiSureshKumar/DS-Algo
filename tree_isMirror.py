def isMirrorUtil(root1, root2):

    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.data==root2.data:
            return (isMirrorUtil(root1.left, root2.right) and isMirrorUtil(root1.right, root2.left))

    else:
        return False

def isMirror(root):

    isMirrorUtil(root, root)


class Tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

root = Tree(1)
root.left = Tree(2)
root.right = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(4)
root.right.left = Tree(4)
root.right.right = Tree(3)
if isMirror(root):
    print("Yes")
else:
    print("No")
