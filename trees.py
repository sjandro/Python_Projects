"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

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
