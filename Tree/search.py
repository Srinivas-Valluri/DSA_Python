from collections import deque

class TreeNode:
  def __init__(self, data) -> None:
    self.data = data
    self.left, self.right = None, None

  def printPreOrder(self,node):
    if node==None:
      return
    print(node.data)
    self.printPreOrder(node.left)
    self.printPreOrder(node.right)

  def search(self, node, val):
    if node==None:
      return "Not Found"
    else:
      q = deque()
      q.append(node)
      while len(q)!=0:
        node=q.popleft()
        if node is None:
          continue
        if node.data==val:
          return "Element Found"
        q.append(node.left)
        q.append(node.right)
        

    return "Not Found"
    


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left = TreeNode(3)

# root.printPreOrder(root)
message = root.search(root, 3)
print(message)

