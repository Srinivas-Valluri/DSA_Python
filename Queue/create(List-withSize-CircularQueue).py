# Better use left and right

class Queue:
  def __init__(self, maxSize) -> None:
    self.queue = [None] * maxSize
    self.start, self.top, self.maxSize = -1,-1, maxSize

  def __str__(self):
    values = [str(x) for x in self.queue]
    return " ".join(values)
  
  def isFull(self):
    if self.top+1==self.start:
      return True 
    elif (self.start==0 and self.top==self.maxSize-1) or (self.top==0 and self.start==self.maxSize-1):
      return True
    else:
      return False
    return
  
  def isEmpty(self):
    if self.top == -1:
      return True
    else:
      return False
    return
  
  def enqueue(self, val):
    if self.isFull():
      return "Queue is Full"
    else:
      if self.top+1==self.maxSize:
        self.top = 0
      else:
        self.top+=1
        if self.start==-1:
          self.start=0
      self.queue[self.top] = val
      return "The element is added at the end of the queue"
    
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      firstElement = self.queue[self.start]
      start = self.start
      if self.start==self.top:
        self.start, self.top = -1,-1
      elif self.start+1==self.maxSize:
        self.start = 0
      else:
        self.start+=1
      return firstElement
    
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      return self.queue[self.start]
    
  def delete(self):
    self.queue = [None] * self.maxSize
    self.start, self.top = -1,-1
    

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q)
print(q.isEmpty())