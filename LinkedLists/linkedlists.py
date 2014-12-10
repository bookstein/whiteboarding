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

