from collections import deque

class BinaryTree:
  def __init__(self, size):
    self.customeList = [None]* size
    self.lastUsedIndex = 0
    self.maxSize = size

  def insert(self, val):
    if self.lastUsedIndex+1 == self.maxSize:
      return "Binary tree is full"
    self.customeList[self.lastUsedIndex+1]=val
    self.lastUsedIndex+=1
    return "the value has been inserted successfully"
  
  def search(self, nodeValue):
    for i in range(len(self.customeList)):
      if self.customeList[i]==nodeValue:
        return "Success"
    return "Not Found"
  
  def preOrder(self, index):
    if index>self.lastUsedIndex:
      return
    print(self.customeList[index])
    self.preOrder(2*index)
    self.preOrder(2*index +1)

  def inOrder(self, index):
    if index>self.lastUsedIndex:
      return
    self.inOrder(2*index)
    print(self.customeList[index])
    self.inOrder(2*index+1)

  def postOrder(self, index):
    if index>self.lastUsedIndex:
      return
    self.postOrder(2*index)
    self.postOrder(2*index+1)
    print(self.customeList[index])

  def levelOrder(self, index): # We can also just print the list items in order...stupid over useage of brain
    if index>self.lastUsedIndex:
      return
    q = deque()
    q.append(self.customeList[index])
    while q:
      curr = q.popleft()
      index = self.customeList.index(curr)
      print(curr)
      if 2*index<=self.lastUsedIndex:
        q.append(self.customeList[2*index])
      if 2*index+1<=self.lastUsedIndex:
        q.append(self.customeList[2*index+1])
    return
  
  def deleteNode(self, val):
    if self.lastUsedIndex==0:
      return "Tree is empty"
    elif self.customeList[self.lastUsedIndex] == val:
      self.lastUsedIndex-=1
    else:
      index = self.customeList.index(val)
      self.customeList[index]=self.customeList[self.lastUsedIndex]
      self.lastUsedIndex-=1
    return
  
  def delete(self):
    self.customeList = [None]*self.maxSize
    self.lastUsedIndex=0
    return


    


newBT = BinaryTree(8)
print(newBT.insert("Drinks"))
print(newBT.insert("Hot"))
print(newBT.insert("Cold"))
print(newBT.insert("Tea"))
print(newBT.insert("Coffee"))

newBT.preOrder(1)
print("-------------")
newBT.inOrder(1)
print("-------------")
newBT.postOrder(1)
print("-------------")
newBT.levelOrder(1)