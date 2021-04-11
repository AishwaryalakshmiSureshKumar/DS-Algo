def BTtoDLLUtil(root, prev, result):
    if root is None:
        return 0
    else:
        right = root.right
        BTtoDLLUtil(root.left, prev, result)

        if len(prev)==0:
            prev.append(root)
        else:
            prev[0].right = root
            root.left = prev[0]
            prev[0] = root

        if len(result)==0:
            result.append(root)

        BTtoDLLUtil(root.right, prev, result)

def BTtoDLL(root):
    result = []
    BTtoDLLUtil(root, [], result)
    return result[0]

def printDLL(head):
    prev = None
    while head!=None:
        print(head.data, end=' ')
        prev = head
        head = head.right
    print()
    while prev!=None:
        print(prev.data, end= ' ')
        prev = prev.left
    print()
        

class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.left.left = Tree(40)
root.left.right = Tree(60)
head = BTtoDLL(root)
printDLL(head)
