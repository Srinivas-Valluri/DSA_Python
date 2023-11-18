class Heap:
  def __init__(self, size) -> None:
    self.customList = [None]*(size+1)
    self.heapSize = 0
    self.maxSize = size+1

def peekofHeap(rootNode): #Time-O(1) Space-O(1)
  if not rootNode:
    return
  else:
    return rootNode.customList[1]
  
def sizeofHeap(rootNode): #Return N.O. of filled nodes #Time-O(1) Space-O(1)
  if not rootNode:
    return None
  else:
    return rootNode.heapSize

def levelOrder(rootNode): #Time-O(N) Space-O(1)
  if not rootNode:
    return
  else:
    for i in range(1, rootNode.heapSize+1):
      print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType):#index=node we want to adjust #Time-O(LogN) Space-O(LogN)
  parentIndex = int(index/2)
  if index<=1:
    return
  if heapType=="Min":
    if rootNode.customList[index]<rootNode.customList[parentIndex]:
      temp = rootNode.customList[index]
      rootNode.customList[index] = rootNode.customList[parentIndex]
      rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex, heapType)
  elif heapType=="Max":
    if rootNode.customList[index]>rootNode.customList[parentIndex]:
      temp = rootNode.customList[index]
      rootNode.customList[index] = rootNode.customList[parentIndex]
      rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex, heapType)

def insert(rootNode, nodeVal, heapType): #Time-O(LogN) Space-O(LogN)
  if rootNode.heapSize+1==rootNode.maxSize:
    return "The Binary Heap is full"
  rootNode.customList[rootNode.heapSize+1]=nodeVal
  rootNode.heapSize+=1
  heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
  return "The value has been successfully inserted"

def heapifyTreeExtract(rootNode, index, heapType):
  leftIndex = 2*index
  rightIndex = 2*index+1
  swapChild=0
  if rootNode.heapSize<leftIndex:
    return
  elif rootNode.heapSize==leftIndex:
    if heapType=="Min":
      if rootNode.customList[index]>rootNode.customList[leftIndex]:
        tempNode = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[leftIndex]
        rootNode.customList[leftIndex] = tempNode
      return
    else:
      if rootNode.customList[index]<rootNode.customList[leftIndex]:
        tempNode = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[leftIndex]
        rootNode.customList[leftIndex] = tempNode
      return
  else:
    if heapType=="Min":
      swapChild = leftIndex if rootNode.customList[leftIndex]<rootNode.customList[rightIndex] else rightIndex
      if rootNode.customList[index]>rootNode.customList[swapChild]:
        tempNode = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[swapChild]
        rootNode.customList[swapChild] = tempNode
    else:
      swapChild = leftIndex if rootNode.customList[leftIndex]>rootNode.customList[rightIndex] else rightIndex
      if rootNode.customList[index]<rootNode.customList[swapChild]:
        tempNode = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[swapChild]
        rootNode.customList[swapChild] = tempNode
    heapifyTreeExtract(rootNode, swapChild, heapType)
      
def extractNode(rootNode, heapType): #Time-O(LogN) Space-O(LogN)
  if rootNode.heapSize==0:
    return
  else:
    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize-=1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode
  
def delete(rootNode):
  rootNode.customList = None
  rootNode.heapSize = 0
  return

newBH = Heap(5) #Time-O(1) Space-O(N)
insert(newBH, 4, "Max")
insert(newBH, 5, "Max")
insert(newBH, 2, "Max")
insert(newBH, 1, "Max")
print(extractNode(newBH, "Max"))
delete(newBH)
levelOrder(newBH)

