# make a Binary Search Tree


class Node(object):
    # in this model, initialize each node outside of the tree (n = Node(7))
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def append_node(self, value):
        print "beginning of append node"
        new_node = Node(value)

        if not self.root:
            # if there's no root (e.g. this is first node),
            # set root to new node
            self.root = new_node
            print "ROOT", self.root
        else:
            # start search at root
            # "node" is a marker for where we currently are
            node = self.root

            while node:  # checks if you're at a node that's not null

                print "top of loop"

                if new_node.value < node.value and node.left:
                    # if node exists to the left, move left --> new root
                    print "Searching left node"
                    print "Left node:", node.left.value
                    node = node.left
                    print "left node after reassignent: ", node, node.value

                elif new_node.value < node.value and not node.left:
                    # set node.left to new_node (add to tree)
                    node.left = new_node
                    print "Set new node on left"
                    return  # exit while loop and function

                elif new_node.value > node.value and node.right:
                    # checks if node to right exists, move right --> new root
                    print "Searching right node"
                    print "Right node:", node.right.value
                    node = node.right

                elif new_node.value > node.value:
                    # set node.right to new_node (add to tree)
                    print "Set new node on left"
                    node.right = new_node
                    return  # exit while loop and function

                elif new_node.value == node.value:
                    print "Duplicate"
                    break  # breaks loop

            return  # exit from function

    def search(self, value):

        """Linear search of tree"""

        node = self.root

        while node:
            if node.value > value:
                node = node.left

            elif node.value < value:
                node = node.right

            elif node.value == value:
                return node.value

            else:
                print "Not found"
                break

            return

    def r_search(self, value, node=None):

        """Recursive search of tree"""

        if not node:
            node = self.root

        while node:

            if node.value > value and node.left:
                return self.r_search(value, node.left)

            elif node.value < value and node.right:
                return self.r_search(value, node.right)

            elif node.value == value:
                return node

            else:
                return "Not found"
                break

t = BinarySearchTree()
t.append_node(10)
t.append_node(3)
t.append_node(1)


# this tree ignores duplicates! --> make sure to say that.
# clarity is IMPORTANT!
