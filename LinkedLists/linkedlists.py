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
    found = False
    node = self.head

    while not found:
      found = True

      if node.data == data:
        return found

      else:
        node = node.next
        found = False


ll = LinkedList()
ll.add(10)
ll.add(5)
ll.add(11)
ll.add(4)
ll.add(100)
ll.add(3)

