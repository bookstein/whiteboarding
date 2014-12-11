class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, data):
    node = Node(data)

    if not self.head:
      self.head = node

    if self.tail is not None:
      # if tail exists, point old tail to new node
      self.tail.next = node
      # the new node becomes the tail
      self.tail = node

    # if no tail exists yet:
    self.tail = node

  def printList(self):
    node = self.head

    while node:
      print node.data
      node = node.next

  def search(self, data):
    node = self.head

    while node != None:

      if node.data == data:
        return node

      else:
        node = node.next

    print "Not found"

  def r_search(self, data, node=None):
    """Recursive search for node by data"""

    if not node:
      node = self.head

    # base case: found data
    if node.data == data:
      return node

    if node.next:
      return self.r_search(data, node.next)

    print "Not found"

  def delete(self, data):
    """Delete a node after finding it by data"""
    current = self.head
    prev = None

    while current.next is not None:

      if current.data == data:
        if not prev:
          self.head = current.next
          current.next = None

        prev.next = current.next
        return # otherwise this was an endless while loop

      else:
        prev = current
        current = current.next





ll = LinkedList()
ll.add(10)
ll.add(5)
ll.add(11)
ll.add(4)
ll.add(100)
ll.add(3)

