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
    """
    DFT, recursive
    pre-ordered because print comes first (prints root) before recursive calls
    """
    print node.value

    # if a node to the left exists, go to it
    if node.left:
        depth_first_traversal(node.left)
    # if a node to the left does not exist, go right
    if node.right:
        depth_first_traversal(node.right)

    # if neither of these conditions are met, function returns None
    print "done with this scope"

def nr_depth_first_traversal(node):
    """
    Non-recursive depth first traversal
    """
    done = False

    while not done:
        print node.value
        prev = node

        if node.left:
            node = node.left
            continue

        if node.right:
            node = node.right
            continue

        else:
            node = prev

def breadth_first_traversal(node):
    if not node:
        return None

    else:
        queue = [node]
        while len(queue) > 0:
            current = queue.pop(0)
            print current.value

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


root = BinaryTreeNode(0)
left = BinaryTreeNode(1)
right = BinaryTreeNode(4)
l_left = BinaryTreeNode(2)
l_right = BinaryTreeNode(3)
r_left = BinaryTreeNode(5)
r_right= BinaryTreeNode(6)
root.set_left(left)
root.set_right(right)
left.set_left(l_left)
left.set_right(l_right)
right.set_left(r_left)
right.set_right(r_right)





