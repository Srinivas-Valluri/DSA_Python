class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("cold")
newBT.left, newBT.right = leftChild, rightChild

def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.left)
  preOrderTraversal(rootNode.right)

preOrderTraversal(newBT)