class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

  def get_value(self):
    return self.value
  
  def get_next(self):
    return self.next 
  
  def set_next(self, new_node):
    self.next = new_node

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value, None)
    
    if self.tail is None:
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    
    if not self.head:
      return None
    
    if not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    
    else:
      value = self.head.get_value()
      self.head = self.head.get_next()
      return value

  def contains(self, value):
    if not self.head:
      return False

    else:
      current = self.head
      while current: 
        if value == current.get_value():
          return True
        else:
          current = current.get_next()
      return False

  def add_to_head(self, value):
    new_node = Node(value, None)

    if not self.head:
        self.head = new_node
        self.tail = new_node 

    elif not self.head.get_next():
        new_node.set_next = self.head
        self.head = new_node
     
    else:
        prev_head = self.head
        self.head = new_node
        self.head.set_next(prev_head)

class Queue: 
  def __init__(self):
      
      # counter to keep track of the number of elements in our queue
      self.size = 0
  
      # Let's use our LinkedList implementation to hold our queue
      self.storage = LinkedList()

  def enqueue(self, item):
      # add the item to the linked_list
      self.storage.add_to_tail(item)
      self.size += 1

  def dequeue(self):
      # decrement our size counter
      if self.size > 0:
          self.size -= 1
      # remove the head of the linked list and return it
      return self.storage.remove_head()

  def len(self):
      return self.size
