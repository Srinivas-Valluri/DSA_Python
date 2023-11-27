import heapq

#class for edges
class Edge:
  def __init__(self, weight, start_vertex, target_vertex):
    self.weight = weight
    self.start_vertex = start_vertex
    self.target_vertex = target_vertex

#class for Nodes
class Node:
  def __init__(self, name) -> None:
    self.name = name
    self.visited = False
    # previous node that we come to this node
    self.predecessor = None
    self.neighbours = []
    self.min_distance = float('inf')

  def __lt__(self, other_node):
    return self.min_distance < other_node.min_distance
  
  def add_edge(self, weight, destination_vertex):
    edge = Edge(weight, self, destination_vertex)
    self.neighbours.append(edge) 

#Dijkstra Algorithm
class Dijkstra:
  def __init__(self):
    self.heap = []

  def calculate(self, start_vertex):
    start_vertex.min_distance = 0
    heapq.heappush(self.heap, start_vertex)
    while self.heap:
      # pop element with the lowest distance
      actual_vertex = heapq.heappop(self.heap)
      if actual_vertex.visited:
        continue  
      # consider neighbour
      for edge in actual_vertex.neighbours:
        start = edge.start_vertex
        target = edge.target_vertex
        new_distance = start.min_distance + edge.weight
        if new_distance<target.min_distance:
          target.min_distance = new_distance
          target.predecessor = start
          #update heap
          heapq.heappush(self.heap, target)
          # [F-19, F-17] instead of updating the value, we do lazy implementation. Instead of updating F we set F to visited
      actual_vertex.visited = True
    
  def get_shortest_path(self, vertex): #here vertex is end vertex cuz the start vertex is given in dijkstra's algorithm
    print(f"The shortest path to the vartex is: {vertex.min_distance}")
    actual_vertex = vertex
    while actual_vertex is not None:
      print(actual_vertex.name, end=" ")
      actual_vertex = actual_vertex.predecessor


#step1 - Create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

#step2 - Create edges
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(6, nodeB)

nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)
nodeB.add_edge(5, nodeD)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)