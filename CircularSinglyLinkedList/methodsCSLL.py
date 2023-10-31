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
  
  def prepend(self, val):
    if self.length==0:
      self.append(val)
      self.length+=1
      return
    newNode = Node(val)
    self.tail.next = newNode
    newNode.next = self.head
    self.head = newNode
    self.length+=1

  def insert(self, val, index):
    self.length+=1
    newNode = Node(val)
    temp = self.head
    if index==1:
      self.tail.next = newNode
      newNode.next = self.head
      self.head=newNode
      return
    if index>self.length:
      self.tail.next = newNode
      newNode.next = self.head
      self.tail=newNode
      return 
    for _ in range(index-2):
      temp = temp.next
    newNode.next = temp.next
    temp.next = newNode
    

  
csl = CSLinkedList()
csl.prepend(5)
csl.append(10)
csl.append(20)
csl.prepend(4)
csl.insert(3.5,1)
csl.insert(3.9,2)
csl.insert(3.7,2)
csl.insert(15,7)
csl.insert(150,9)
print(csl)

