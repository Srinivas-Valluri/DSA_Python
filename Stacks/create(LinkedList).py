class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None

  def __iter__(self):
    currNode = self.head
    while currNode:
      yield currNode
      currNode = currNode.next

class Stack:
  def __init__(self) -> None:
    self.linkedList = LinkedList()

  def __str__(self):
    values = [str(i.val) for i in self.linkedList]
    return "\n".join(values)

  def push(self, val):
    newNode = Node(val)
    newNode.next = self.linkedList.head
    self.linkedList.head = newNode

  def pop(self):
    if self.isEmpty():
      return "There is nothing in the stack"
    else:
      nodeValue = self.linkedList.head.val
      self.linkedList.head = self.linkedList.head.next
      return nodeValue
  
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    else:
      return self.linkedList.head.val

  def isEmpty(self):
    return True if not self.linkedList.head else False
  
  def delete(self):
    self.head = None

st = Stack()
st.push(1)
st.push(2)
st.push(3)
print(st)
st.pop()
print("After pop")
print(st)
print(f"Peek: {st.peek()}")
print(st.isEmpty())