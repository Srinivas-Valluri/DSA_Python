class Queue:
  def __init__(self) -> None:
    self.queue = []
    self.size = 0

  def __str__(self):
    values = [str(x) for x in self.queue]
    return " ".join(values)

  def enqueue(self, val):
    self.queue.append(val)
    return "Element is added at the end"

  def dequeue(self):
    if self.isEmpty():
      return "No element in Queue"
    else:
      return self.queue.pop(0)
  
  def peek(self):
    if self.isEmpty():
      return "No element in Queue"
    else:
      return self.queue[0]
  
  def isEmpty(self):
    return True if self.queue == [] else False
  
  
  def delete(self):
    self.queue = []

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.peek())
print(q)
q.delete()
print(q)