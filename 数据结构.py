#coding=utf-8

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if treeNode.lchild == Node:
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == Node:
                    treeNode.rchild = node
                    return
                else:
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print root.elem,
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

