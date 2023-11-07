class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("cold")
newBT.left, newBT.right = leftChild, rightChild

def inOrderTraversal(rootNode):
  if not rootNode:
    return
  
  inOrderTraversal(rootNode.left)
  print(rootNode.data)
  inOrderTraversal(rootNode.right)

inOrderTraversal(newBT)