class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    value = str(self.val)
    if self.next:
      value += ','+str(self.val)
    return value
    

class Stack:
  def __init__(self) -> None:
    self.top, self.minNode = None, None

  def min(self):
    if not self.minNode:
      return None
    return self.minNode.val
  
  def push(self, val):
    if self.minNode and (self.minNode.val<val):
      self.minNode = Node(val=self.minNode.val, next=self.minNode)
    else:
      self.minNode = Node(val = val, next=self.minNode)
    self.top = Node(val=val, next=self.top)

  def pop(self):
    if not self.top:
      return "Stack is Empty"
    popValue = self.top.val
    self.top = self.top.next
    self.minNode = self.minNode.next
    return popValue
    

customStack = Stack()
customStack.push(3)
print(customStack.min())
customStack.push(4)
print(customStack.min())
customStack.push(1)
print(customStack.min())
print("pop value: ", customStack.pop())
print(customStack.min())
customStack.push(10)
print(customStack.min())