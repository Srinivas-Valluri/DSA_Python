class PlateStack:
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.stacks = []

  def __str__(self) -> str:
    return self.stacks

  def push(self, item):
    if len(self.stacks)>0 and (len(self.stacks[-1])<self.capacity):
      self.stacks[-1].append(item)
    else:
      self.stacks.append([item])

  def pop(self):
    while len(self.stacks) and len(self.stacks[-1])==0:
      self.stacks.pop()
    if len(self.stacks)==0:
      return None
    else:
      return self.stacks[-1].pop()
    
  def pop_at(self, stacknum):
    if len(self.stacks[stacknum]):
      return self.stacks[stacknum].pop()
    else:
      return "sub-stack is empty"

customeStack = PlateStack(2)
customeStack.push(1)
customeStack.push(2)
customeStack.push(3)
customeStack.push(4)
print(customeStack.pop_at(0))