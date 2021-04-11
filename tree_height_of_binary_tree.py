def height(root):
    # code here
    if root==None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        
        if (lheight > rheight):
            return lheight+1
        else:
            return rheight+1