# for a linked list, find maximum value reachable from a given node
class Node(object):
    def __init__(next, data):
        next.data = data
        next.next = None


def find_next_biggest(node):
    """
    Find the next biggest number in a linked list from any given node.
    """
    # set biggest_num to current node data
    biggest_num = node.data

    # while a next node exists
    while node.next:
        # change value of biggest_num only if next node has bigger data val
        if node.next.data > biggest_num:
            biggest_num = node.next.data
            print "biggest num is now ", biggest_num

        # change current node to next node until no next node exists
        node = node.next

    return biggest_num


def r_find_next_biggest(node):
    """
    Find the next biggest number in a linked list from any given node,
    recursively.
    """
    pass
    # base case: only one node exists (no next node)
    if not node.next:
        return node.data

    else:
        if node.next.data > node.data:
            return r_find_next_biggest(node.next)


a = Node(2)
b = Node(7)
c = Node(2)
d = Node(10)
e = Node(1)
f = Node(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
