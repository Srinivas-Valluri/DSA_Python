class Node:
  def __init__(self, value) -> None:
    self.next = None
    self.value = value

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def insertAtStart(self, value):
    if self.head == None:
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length += 1
    else:
      new_node = Node(value)
      new_node.next = self.head
      self.head=new_node
      self.length += 1

  def __str__(self):
    values = []
    curr_node = self.head
    while curr_node:
      values.append(curr_node.value)
      curr_node = curr_node.next
    return str(values)


linkedList = LinkedList()
linkedList.insertAtStart(10)
print(linkedList)
linkedList.insertAtStart(20)
print(linkedList)
linkedList.insertAtStart(30)
print(linkedList)


    