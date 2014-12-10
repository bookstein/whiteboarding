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
    biggest_num = node.data

    # base case: if current node is only node (node.next --> None)
    if not node.next:
        return biggest_num # node.data

    print "before recursion"

    next_biggest = r_find_next_biggest(node.next)

    print "past recursion"

    if next_biggest > biggest_num: # greater than node.data
        biggest_num = next_biggest

    return biggest_num

# OLD VERSION
# def r_find_next_biggest(node, biggest_num=None):
#     """
#     Find the next biggest number in a linked list from any given node,
#     recursively.
#     """
#     if not biggest_num:
#         biggest_num = node.data

#     # base case: if current node is None (node.next --> None)
#     if not node:
#         # this only runs once
#         return biggest_num

#     else:
#         # change value of biggest num
#         if node.data >= biggest_num:
#             biggest_num = node.data

#         # why does this need to return? --> REMEMBER!
#           # BECAUSE otherwise, coming back up, each function returns None
#         return r_find_next_biggest(node.next, biggest_num)


#         # # work on this! START HERE TOMORROW (this invalidates other stuff!)
#         # next_biggest = r_find_next_biggest(node.next)
#         # if next_biggest > node.data:
#         #     return next_biggest


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
