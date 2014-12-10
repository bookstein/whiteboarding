# I'm going to try to remember to send out one real-world interview question every day over the next couple of weeks. Since today we talked about linked lists, this one can be solved with a linked list. It can be solved without it as well. Try to figure it out both ways. I will tell you the answer if you show me your code and what your code spits out.

# Today's question:
# You are in a room with a circle of 100 chairs. The chairs are numbered sequentially from 1 to 100.

# At some point in time, the person in chair #1 will be asked to leave. The person in chair #2 will be skipped, and the person in chair #3 will be asked to leave. This pattern of skipping one person and asking the next to leave will keep going around the circle until there is one person left the survivor.

# Write a program to determine which chair the survivor is sitting in.


class Node(object):
    def __init__(self, number=None, next=None):
        self.number = number
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def insert(self, number):
        """Insert nodes into list"""
        new_node = Node(number)

        # if no head, set node to be head
        if not self.head:
            self.head = new_node

        # if the tail already exists, set tail to new node
        if self.tail:
            #previous tail must point to new node
            self.tail.next = new_node

        # new node becomes the tail
        self.tail = new_node


    def make_circuluar(self):
        """
        Closes the loop by pointing the given tail to the head
        """
        if not self.tail.next:
            self.tail.next = self.head


    def r_remove(self, node=None):
        """
        Recursively travel down the linked list and remove every other node
        """

        if not node:
            node = self.tail

        #base case: when node points to itself
        if node.next == node:
            return node.number

        else:
            node.next = node.next.next
            return self.r_remove(node.next)


ll = LinkedList()
for i in range(1, 101):
    ll.insert(i)
ll.make_circuluar()

