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

  def insert(self, index, data):
    """
    Insert a node with value 'data' at any point by specifying index (or count)
    Index is the position after which node will be inserted.
    Count starts at 0.
    """
    node = Node(data)
    current = self.head
    count = 0

    while count <= index:

      if index == 0:
        node.next = current
        self.head = node
        return

      if count == index:
        node.next = current.next
        current.next = node

      count += 1
      current = current.next

  def length(self):
    """
    Length of list
    """
    count = 0
    current = self.head
    is_end = False

    while not is_end:
      count += 1

      if not current.next:
        is_end = True

      current = current.next


    return count

  def get_index(self, data):
    """
    Get index of node using given data (essentially search but with count)
    Count is zero-indexed
    """
    count = 0
    current = self.head

    while current:  # after last node of list, current is None
      if current.data == data:
        print count
        return

      else:
        current = current.next
        count += 1

    return "Not found"

  def find_max(self, current=None):
    """Find max value in a list"""
    if not current:
      current = self.head

    # base case: only 1 number in list
    if not current.next:
      return current.data

    else:
      bigger = self.find_max(current.next)

      if bigger < current.data:
        bigger = current.data

    return bigger

  def find_min(self, current=None):
    """Find min value in a list"""
    if not current:
      current = self.head

    # base case: list has 1 value
    if not current.next:
      return current.data

    else:
      smaller = self.find_min(current.next)

      if current.data < smaller:
        smaller = current.data

    return smaller


ll = LinkedList()
ll.add(10)
ll.add(5)
ll.add(11)
ll.add(4)
ll.add(100)
ll.add(3)

