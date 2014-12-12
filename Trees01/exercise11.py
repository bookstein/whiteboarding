class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def set_value(self, number):
        self.value = number

def depth_first_traversal(node):
    print node.value

    # if a node to the left exists, go to it
    if node.left:
        depth_first_traversal(node.left)
    # if a node to the left does not exist, go right
    if node.right:
        depth_first_traversal(node.right)

    # if neither of these conditions are met, function returns None
    print "done with this scope"




