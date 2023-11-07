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
  

q = Queue()
print(q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(1)
print(q.peek())
print(q)





  