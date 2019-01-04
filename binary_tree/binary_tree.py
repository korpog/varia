class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse_preorder(root): 

    if root: 

        print(root.value)

        traverse_preorder(root.left) 

        traverse_preorder(root.right) 


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    traverse_preorder(root)
