def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)

class Tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

root = Tree(4)
root.left = Tree(8)
root.right = Tree(10)
root.left.left = Tree(7)
root.left.left.left = Tree(3)
root.right.left = Tree(5)
root.right.right = Tree(1)
print(countLeaves(root))
