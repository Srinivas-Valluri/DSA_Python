from collections import deque

class TreeNode:
  def __init__(self, data) -> None:
    self.data = data
    self.left, self.right = None, None

  def insert(self, rootNode, val):
    if rootNode==None:
      self.__init(val)
      return
    else:
      newNode = TreeNode(val)
      q = deque()
      q.append(rootNode)
      while q:
        popNode=q.popleft()
        if popNode.left==None:
          popNode.left=newNode
          return
        if popNode.right==None:
          popNode.right = newNode
          return
        q.append(popNode.left)
        q.append(popNode.right)

  def inOrder(self, rootNode):
    if rootNode==None:
      return
    self.inOrder(rootNode.left)
    print(rootNode.data)
    self.inOrder(rootNode.right)


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left = TreeNode(3)
root.insert(root, 5)
root.inOrder(root)