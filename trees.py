"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

class Node(object):
    """docstring for """
    def __init__(self, data, left = None ,right = None):
        super(Node,self).__init__()
        self.data = data
        self.left = left
        self.right = right


def inOrder(root):
    if root:
        if root.left:
            inOrder(root.left)
        sys.stdout.write(str(root.data) + " ")
        if root.right:
            inOrder(root.right)


def preOrder(root):
    if root:
        sys.stdout.write(str(root.data) + " ")
    if root.left:
        preOrder(root.left)
        if root.right:
            preOrder(root.right)

def postOrder(root):
    if root:
        if root.left:
            postOrder(root.left)
            if root.right:
                postOrder(root.right)
        sys.stdout.write(str(root.data) + " ")

def insertToTree(root, data):
    if root:
        if root.data < data:
            if not root.right:
                root.right = Node(data)
            else:
                insertToTree(root.right, data)
        else:
            if not root.left:
                root.left = Node(data)
            else:
                insertToTree(root.left, data)



def main():
    head = Node(10)

    for i in [3,2,65,2,12,32,5]:
        insertToTree(head, i)

    inOrder(head)
    print "\n"
    preOrder(head)
    print "\n"
    postOrder(head)

if __name__ == '__main__':
    main()
