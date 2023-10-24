# class Node:
#   def __init__(self, value) -> None:
#     self.value = value
#     self.next = None

# class LinkedList:
#   def __init__(self, value) -> None:
#     new_node = Node(value)
#     self.head = new_node
#     self.tail = new_node
#     self.length = new_node

class LinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.length = 0

ll = LinkedList()

print(ll.head)
