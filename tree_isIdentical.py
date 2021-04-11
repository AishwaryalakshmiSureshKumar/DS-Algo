def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None and root2 is not None:
        return False

    if root1 is not None and root2 is None:
        return False

    if root1.data!=root2.data:
        return False

    if root1.data==root2.data:
        return True and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

class Tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

root1 = Tree(1)
root1.left = Tree(2)
root1.right = Tree(3)
root2 = Tree(1)
root2.left = Tree(2)
root2.right = Tree(3)
if isIdentical(root1, root2):
    print("Identical")
else:
    print("Not Identical")
