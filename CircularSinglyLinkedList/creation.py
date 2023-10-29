#Node class remains same as single linked list

class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.next = None
    
## Creation of CSL with one node.
# class CSLinkedList:
#   def __init__(self, val) -> None:
#     new_node = Node(val)
#     new_node.next = new_node
#     self.head = new_node
#     self.tail = new_node
#     self.length = 1

# Creation of CSL with no nodes.
class CSLinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.length = 1

cslinkedlist = CSLinkedList()
print(cslinkedlist.head)