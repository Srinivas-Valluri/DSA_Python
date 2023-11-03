class Stack:
  def __init__(self, maxSize):
    self.list = []
    self.maxSize = maxSize

  def __str__(self) -> str:
    values = reversed(self.list)
    values = [str(x) for x in values]
    return "\n".join(values)
  
  def isEmpty(self):
    return True if len(self.list)==0 else False
  
  def isFull(self):
    if len(self.list)==self.maxSize:
      return True
    else:
      return False
  
  def push(self, val):
    if len(self.list)>=self.maxSize:
      return print(f"No room to add an element {val}")
    else:
      self.list.append(val)
      return "The element is added to stack"
  
  def pop(self):
    return "No element in Stack" if self.isEmpty() else self.list.pop()
  
  def peek(self):
    return "No element in Stack" if self.isEmpty() else self.list[-1]
  
  def delete(self):
    self.list = None
  

st = Stack(2)
st.push(1)
st.push(2)
st.push(3)
print(st)
st.pop()
print("After pop")
print(st)
print(f"Peek: {st.peek()}")
print(st.isEmpty())