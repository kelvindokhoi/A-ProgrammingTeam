# BST (Binary Search Tree)

class Node():
    def __init__(self,v):
        self.v = v
        self.left = None
        self.right = None

class BST():
    def __init__(self,logic):
        self.root = None
        self.logic = logic
    def inserHelper(self,node,newnode):
        if node is None:
            return newnode
        if self.logic.index(newnode.v) <= self.logic.index(node.v):
            node.left = self.inserHelper(node.left,newnode)
        else:
            node.right = self.inserHelper(node.right,newnode)
        return node
    def insert(self,v):
        newnode = Node(v)
        self.root = self.inserHelper(self.root,newnode)
    
    def postorderPrint(self,currnode):
        if currnode is None:
            return
        a=self.postorderPrint(currnode.left)
        b=self.postorderPrint(currnode.right)
        return (a if a is not None else '')+(b if b is not None else '')+currnode.v
    
    def postorder(self):
        return self.postorderPrint(self.root)


while True:
    try:
        my_preorder, my_inorder = input().split()
        bst = BST(my_inorder)
        for i in my_preorder: #whty the f u use iterator as enumerator????????
            bst.insert(i)
        print(bst.postorder())
    except:
        break


