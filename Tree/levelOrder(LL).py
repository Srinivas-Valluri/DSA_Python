#Upto line 58 queue implementation. then LevelOrder Traversal.

class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

class Queue:
  def __init__(self) -> None:
    self.item = LinkedList()

  def __str__(self):
    if not self.item:
      return "Queue is empty"
    curr = self.item.head
    values = []
    while curr:
      values.append(curr.val)
      curr = curr.next
    return str(values)

  def isEmpty(self):
    return True if self.item.head==None else False

  def enqueue(self, val):
    newNode = Node(val)
    if self.isEmpty():
      self.item.head, self.item.tail = newNode, newNode
    else:
      self.item.tail.next = newNode
      self.item.tail = newNode
    return "Item added to queue"
  
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      dequeueValue = self.item.head.val
      if self.item.head == self.item.tail:
        self.item = LinkedList()
      else:
        self.item.head = self.item.head.next
      return dequeueValue
    
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      return self.item.head.val
    
  def delete(self):
    self.item = LinkedList()

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("cold")
newBT.left, newBT.right = leftChild, rightChild

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    customeQueue = Queue()
    customeQueue.enqueue(rootNode)
    while not customeQueue.isEmpty():
      root = customeQueue.dequeue()
      print(root.data)
      if root.left is not None:
        customeQueue.enqueue(root.left)
      if root.right is not None:
        customeQueue.enqueue(root.right) 

levelOrderTraversal(newBT)


  






  