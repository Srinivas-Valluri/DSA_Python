from collections import deque

class BSTNode:
  def __init__(self, data):
    self.data = data
    self.left, self.right = None, None

def insert(rootNode, val):
  if rootNode.data==None:
    rootNode.data = val
  elif val <= rootNode.data:
    if rootNode.left is None:
      rootNode.left= BSTNode(val)
    else:
      insert(rootNode.left, val)
  else:
    if rootNode.right is None:
      rootNode.right = BSTNode(val)
    else:
      insert(rootNode.right, val)
  return "The node has been successfully inserted"

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

def minValueNode(bstNode):
  curr = bstNode
  while curr.left is not None:
    curr = curr.left
  return curr

def deleteNode(rootNode, nodeValue):
  if rootNode is None:
    return rootNode
  if nodeValue < rootNode.data:
    rootNode.left = deleteNode(rootNode.left, nodeValue)
  elif nodeValue > rootNode.data:
    rootNode.right = deleteNode(rootNode.right, nodeValue)
  else:
    if rootNode.left is None:
      temp = rootNode.right
      rootNode=None
      return temp
    
    if rootNode.right is None:
      temp = rootNode.left
      rootNode=None
      return temp
    
    temp = minValueNode(rootNode.right)
    rootNode.data = temp.data
    rootNode.right = deleteNode(rootNode.right, temp.data)
  return rootNode

def delete(rootNode):
  rootNode.data=None
  rootNode.left=None
  rootNode.right=None
  return "BST is deleted"


newBST = BSTNode(None)
print(insert(newBST, 70))
print(insert(newBST, 50))
print(insert(newBST, 90))
print(insert(newBST, 30))
print(insert(newBST, 60))
print(insert(newBST, 80))
print(insert(newBST, 100))
print(insert(newBST, 20))
print(insert(newBST, 40))
deleteNode(newBST, 20)
# print("-----------------")
# preOrder(newBST)
# print("-----------------")
# inOrder(newBST)
# print("-----------------")
# postOrder(newBST)
# print("-----------------")
levelOrder(newBST)
print("-----------------")
delete(newBST)
print("-----------------")
levelOrder(newBST)
print("-----------------")