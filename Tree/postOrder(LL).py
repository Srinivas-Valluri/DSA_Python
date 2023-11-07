class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("cold")
newBT.left, newBT.right = leftChild, rightChild

def postOrderTraversal(rootNode):
  if not rootNode:
    return
  
  postOrderTraversal(rootNode.left)
  postOrderTraversal(rootNode.right)
  print(rootNode.data)

postOrderTraversal(newBT)