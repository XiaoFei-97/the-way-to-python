#树

class Node(object):
    """节点的类"""

    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    """树的类"""

    def __init__(self):
        self.root = None
        
    def add(self,item):
        """为树添加节点"""

        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root] #用来存放遍历的东西

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    def breadth_travel(self):
        """广度遍历"""
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self,node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        """先序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem)
        self.inorder(node.rchild)
    def postorder(self,node):
        """先序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem)


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.breadth_travel()
    print("")
    tree.preorder(tree.root)
    print("")
    tree.inorder(tree.root)
    print("")
    tree.postorder(tree.root)


