class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head, self.tail, self.length = None, None, 0

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next

  #Creation of Doubly Linked List
  def createDLL(self, nodeValue):
    node = Node(nodeValue)
    node.prev, node.next = None, None
    self.head, self.tail = node, node
    self.length+=1
    return "DLL created successful"
  
  def insert(self, index, val):
    if self.head==None:
      self.createDLL(val)
    newNode = Node(val)
    if index==0:
      newNode.next = self.head
      self.head.prev = newNode
      self.head=newNode
      self.length+=1
      return
    if index>=self.length:
      self.tail.next = newNode
      newNode.prev = self.tail
      self.tail = newNode
      self.length+=1
      return
    
    #insert in middle
    curr = self.head
    while index-1:
      curr=curr.next
      index-=1

    curr.next.prev = newNode
    newNode.next = curr.next
    curr.next = newNode
    newNode.prev = curr
    self.length+=1
    

  

  
dll = DoublyLinkedList()
dll.createDLL(10)
dll.insert(1,20)
dll.insert(1,15)
dll.insert(1,12)
print([node.val for node in dll])
print(dll.length)