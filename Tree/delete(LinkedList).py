# Node doesn't exist. we delete nothing
# Node exist. we find the deepest node and replace the deleted node with this node.

from collections import deque

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.right, self.left = None, None

  def inOrder(self, rootNode):
    if rootNode==None:
      return
    self.inOrder(rootNode.left)
    print(rootNode.data)
    self.inOrder(rootNode.right)

  def getDeepestNode(self, rootNode):
    if rootNode is None:
      return
    q, deepestNode = deque(), None
    q.append(rootNode)
    while q:
      deepestNode = q.popleft()
      if deepestNode.left is not None:
        q.append(deepestNode.left)
      if deepestNode.right is not None:
        q.append(deepestNode.right)
    return deepestNode


  def deleteTheDeepest(self, rootNode):
    if rootNode is None:
      return
    elif rootNode==self.getDeepestNode(rootNode):
      return "Make Tree Empty"
    else:
      deepestNode = self.getDeepestNode(rootNode)
      q= deque()
      q.append(rootNode)
      while q:
        currNode = q.popleft()
        if currNode.left == deepestNode:
          currNode.left=None
          break
        if currNode.right == deepestNode:
          currNode.right=None
          break
        if currNode.left is not None:
          q.append(currNode.left)
        if currNode.right is not None:
          q.append(currNode.right)
      return "Deepest Node Deleted"

  def deleteNode(self, rootNode, delNode):
    if rootNode is None or deepestNode == self.getDeepestNode(rootNode):
      return None
    deepestNode = self.getDeepestNode(rootNode)
    self.deleteTheDeepest(rootNode)
    q = deque()
    q.append(rootNode)
    while q:
      currNode = q.popleft()
      if currNode.left.data == delNode:
        currNode.left.data = deepestNode.data
        break
      if currNode.right.data == delNode:
        currNode.right.data = deepestNode.data
        break
      if currNode.right is not None:
        q.append(currNode.right)
      if currNode.left is not None:
        q.append(currNode.left)
    return rootNode


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left = TreeNode(3)
root.inOrder(root)
print("----------------")
print(root.getDeepestNode(root).data)
print("----------------")
root = root.deleteNode(root, 1)
root.inOrder(root)
