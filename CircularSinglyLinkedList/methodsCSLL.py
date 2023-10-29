class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class CSLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, val):
    new_node = Node(val)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
      new_node.next = self.head
    self.length+=1

  def __str__(self) -> str:
    values = []
    if self.length==0:
      print("CSLL is empty")
      return str(values)
    else:
      values.append(self.head.val)
    curr = self.head.next
    while curr!=self.head:
      values.append(curr.val)
      curr=curr.next
    return str(values)
csl = CSLinkedList()
csl.append(10)
csl.append(20)

print(csl.head.next.val)
print(csl)