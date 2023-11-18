from collections import deque

class AVLTree:
  def __init__(self, data) -> None:
    self.data = data
    self.left, self.right = None, None
    self.height = 1

def preOrder(rootNode):
  if rootNode is None:
    return 
  print(rootNode.data)
  preOrder(rootNode.left)
  preOrder(rootNode.right)

def inOrder(rootNode):
  if rootNode is None:
    return 
  inOrder(rootNode.left)
  print(rootNode.data)
  inOrder(rootNode.right)

def postOrder(rootNode):
  if rootNode is None:
    return 
  postOrder(rootNode.left)
  postOrder(rootNode.right)
  print(rootNode.data)

def levelOrder(rootNode):
  if rootNode is None:
    return
  q = deque()
  q.append(rootNode)
  while q:
    curr = q.popleft()
    print(curr.data)
    if curr.left is not None:
      q.append(curr.left)
    if curr.right is not None:
      q.append(curr.right)
  return

def search(rootNode, nodeVal):
  if rootNode==None:
    print("Not Found")
    return
  elif rootNode.data==nodeVal:
    print("Found")
    return "Found"
  elif nodeVal<=rootNode.data:
    search(rootNode.left, nodeVal)
  else:
    search(rootNode.right, nodeVal)

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.left
    disbalanceNode.left = disbalanceNode.left.right
    newRoot.right = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.right
    disbalanceNode.right = disbalanceNode.right.left
    newRoot.left = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLTree(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left = insertNode(rootNode.left, nodeValue)
    else:
        rootNode.right = insertNode(rootNode.right, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.left.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.right.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
   if not rootNode or rootNode.left is None:
      return rootNode
   return getMinValueNode(rootNode.left)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
      return rootNode
    elif nodeValue<rootNode.data:
      rootNode.left=deleteNode(rootNode.left, nodeValue)
    elif nodeValue>rootNode.data:
      rootNode.right=deleteNode(rootNode.right, nodeValue)
    else:
       if rootNode.left is None:
          temp=rootNode.right
          rootNode=None
          return temp
       elif rootNode.right is None:
          temp=rootNode.left
          rootNode=None
          return temp
       temp = getMinValueNode(rootNode.right)
       rootNode.data = temp.data
       rootNode.right=deleteNode(rootNode.right, temp.data)
    rootNode.height = 1+max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance>1 and getBalance(rootNode.left)>=0:
      return rightRotate(rootNode)
    if balance<-1 and getBalance(rootNode.right)<=0:
       return leftRotate(rootNode)
    if balance>1 and getBalance(rootNode.left)<0:
       rootNode.left=leftRotate(rootNode.left)
       return rightRotate(rootNode)
    if balance<-1 and getBalance(rootNode.left)>0:
       rootNode.right=leftRotate(rootNode.right)
       return leftRotate(rootNode)
    return rootNode

def delete(rootNode):
   rootNode.data=None
   rootNode.left, rootNode.right=None, None
   print("The AVL Tree is deleted")
   return rootNode


newAVL = AVLTree(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = deleteNode(newAVL, 15)
delete(newAVL)
levelOrder(newAVL)

# insert 30, 25, 35, 20, 15, 5,10,50,60,70,65
