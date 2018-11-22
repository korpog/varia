class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def set_left(self, new_left):
        self.left = new_left

    def get_right(self):
        return self.right

    def set_right(self, new_right):
        self.left = new_right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
