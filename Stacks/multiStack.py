class MultiStack:
  def __init__(self, stackSize):
    self.numberStacks = 3
    self.custList = [0] * (stackSize*self.numberStacks)
    self.sizes = [0]*self.numberStacks
    self.stacksize = stackSize

  def isFull(self, stacknum):
    if self.sizes[stacknum] == self.stacksize:
      return True
    else:
      return False
    
  def isEmpty(self, stacknum):
    if self.sizes[stacknum]==0:
      return True
    else:
      return False
    
  def indexOfTop(self, stacknum):
    return self.stacksize*stacknum + self.sizes[stacknum] -1
  
  def push(self, item, stacknum):
    if self.isFull(stacknum):
      return "Stack is full"
    else:
      self.sizes[stacknum]+=1
      self.custList[self.indexOfTop(stacknum)] = item
    return
  
  def pop(self, stacknum):
    if self.isEmpty(stacknum):
      return "Stack is empty"
    else:
      popValue = self.custList[self.indexOfTop(stacknum)]
      self.sizes[stacknum]-=1
      return popValue
    
  def peek(self, stacknum):
    if self.isEmpty(stacknum=stacknum):
      return "Stack is empty. Nothing peek boiye!"
    return self.custList[self.indexOfTop(stacknum)]
  

customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1,0)
customStack.push(2,0)
customStack.push(3,2)
print(customStack.peek(1))
print(customStack.pop(0))
