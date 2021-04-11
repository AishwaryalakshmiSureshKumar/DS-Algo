def connect_nodes_samelevel(root):
    if root is None:
        return 0
    else:
        root.nextRight = None

        if root.left:
            root.left.nextRight = root.right
        if root.right:
            if root.nextRight:
                root.right.nextRight = root.nextRight.left
            else:
                root.right.nextRight = None
        connect_nodes_samelevel(root.left)
        connect_nodes_samelevel(root.right)

class Tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.left.left = Tree(40)
root.left.right = Tree(60)
connect_nodes_samelevel(root)
