class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.next, self.prev = None, None

class CDLList:
  def __init__(self) -> None:
    self.head, self.tail, self.length = None, None, 0

  def create(self, val):
    newNode = Node(val)
    self.head, self.tail = newNode, newNode
    newNode.next, newNode.prev = newNode, newNode
    self.length+=1
    return "CDLL created sucessfully"

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
      if node == self.tail.next:
        break

  def insert(self, index, val):
    if self.length==0:
      self.create(val)
    else:
      newNode = Node(val)
      index = index if (index<self.length or index==0) else self.length-1
      if index==0:
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.tail.next = newNode
        newNode.prev = self.tail
      elif index==self.length-1:
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.tail.next = self.head
        self.head.prev = self.tail
      else:
        curr = self.head
        while index-1:
          curr = curr.next
          index-=1
        newNode.next = curr.next
        curr.next.prev = newNode
        curr.next = newNode
        newNode.prev = curr
      self.length+=1




  
cdll = CDLList()
print(cdll.create(5))
cdll.insert(0,1)
cdll.insert(0,0)
cdll.insert(3,10)
cdll.insert(1,0.5)
cdll.insert(2,0.9)
print([node.val for node in cdll])

