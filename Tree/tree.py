#Basic Tree with children as list of TreeNode.

class TreeNode:
  def __init__(self, data, children=[]):
    self.data = data
    self.children = children

  def __str__(self, level=0):
    ret = " "* level + str(self.data) + "\n"
    for child in self.children:
      ret+= child.__str__(level+1)
    return ret
  
  def addChild(self, child):
    self.children.append(child)


Tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
Tree.addChild(cold)
Tree.addChild(hot)
fanta = TreeNode('fanta', [])
cola = TreeNode('cola', [])
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])

cold.addChild(fanta)
cold.addChild(cola)
hot.addChild(tea)
hot.addChild(coffee)
print(Tree)
