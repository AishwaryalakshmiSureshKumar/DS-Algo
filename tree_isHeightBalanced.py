def isBal(root):
    if root is None:
        return True, 0
    left, lh = isBal(root.left)
    if not left:
        return False, 0
    right, rh = isBal(root.right)
    if not right:
        return False, 0

    if abs(lh-rh)>1:
        return False, 0

    return True, max(lh,rh)+1

def isBalanced(root):

    result, _ = isBal(root)
    print(_)
    return result

class Tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.left.left = Tree(40)
root.left.right = Tree(60)
if isBalanced(root):
    print("Balanced")
else:
    print("Not Balanced")
