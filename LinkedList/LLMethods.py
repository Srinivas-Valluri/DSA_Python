class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
      self.head = None
      self.tail = None
      self.length = 0

    def append(self, value):
      new_node = Node(value)
      if self.head is None:
          self.head = new_node
          self.tail = new_node
      else:
          self.tail.next = new_node
          self.tail = new_node
      
      self.length += 1

    def __str__(self):
      values = ""
      current = self.head
      while current:
          values+=(str(current.value)+("->" if current.next else " "))
          current = current.next
      return str(values)
    
    def insertAtStart(self, value):
      new_node = Node(value)
      if self.head == None:
        self.head = new_node
        self.tail = new_node
      else:
        new_node.next = self.head
        self.head=new_node
      self.length += 1

    def insertAt(self, index, value):
      new_node = Node(value)
      self.length+=1
      if index==1:
        new_node.next = self.head
        self.head=new_node
      elif self.length<index:
         if self.head==None:
            self.head = new_node
            self.tail = new_node
         self.tail.next = new_node
         self.tail = new_node
      else:
        curr = self.head
        for i in range(1, index-1):
          curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
      return None
    


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.insertAtStart(5)
print(ll)
print(ll.head.value)
print(ll.tail.value)
print(ll.length)
ll.insertAt(1,2)
print(ll)
ll.insertAt(4, 50)
print(ll)
ll.insertAt(10, 100)
print(ll)
print(ll.length)
print(ll.head.value)
print(ll.tail.value)
