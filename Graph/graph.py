from collections import deque

class Graph:
  def __init__(self, gdict=None) -> None:
    if not gdict:
      gdict={}
    self.gdict = gdict

  def add_vertex(self, vertex):
    if vertex not in self.gdict.keys():
      self.gdict[vertex] = []
      return True
    return False

  def printGraph(self):
    for vertex in self.gdict:
      print(vertex,":",self.gdict[vertex])

  def addEdge(self, vertex1, vertex2):
    if vertex1 not in self.gdict.keys() or vertex2 not in self.gdict.keys():
      return False
    else:
      self.gdict[vertex1].append(vertex2)
      self.gdict[vertex2].append(vertex1)
    return True
    
  def removeEdge(self, vertex1, vertex2):
    if (vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys()) and (vertex2 in self.gdict[vertex1] and vertex1 in self.gdict[vertex2]):
      self.gdict[vertex1].remove(vertex2)
      self.gdict[vertex2].remove(vertex1)
      return True
    return False
  
  def removeVertex(self, vertex):
    #checking for correctness of graph
    for i in self.gdict[vertex]:
      if i in self.gdict.keys() and vertex in self.gdict[i]:
        pass
      else:
        print("Something Wrong with Graph")
        return False
    #After checking we start removing
    for i in self.gdict[vertex]:
      self.gdict[i].remove(vertex)
    self.gdict.pop(vertex)
    return True
  
  def bfs(self, vertex): #Time-O(V+E) Space-O(V+E)
    visited = set()
    visited.add(vertex)
    q = deque([vertex])
    while q:
      current_vertex = q.popleft()
      print(current_vertex)
      for adjacent_vertex in self.gdict[current_vertex]:
        if adjacent_vertex not in visited:
          visited.add(adjacent_vertex)
          q.append(adjacent_vertex)

  def dfs(self, vertex): #Time-O(V+E) Space-O(V+E) 
    visited = set()
    stack = deque([vertex])
    while stack:
      current_vertex = stack.pop()
      if current_vertex not in visited:
        print(current_vertex)
        visited.add(current_vertex)
      for adjacent_vertex in self.gdict[current_vertex]:
        if adjacent_vertex not in visited:
          stack.append(adjacent_vertex)

  

customDict = {}
    
graph = Graph(customDict)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("B", "E")
graph.addEdge("D", "E")
graph.addEdge("C", "D")
graph.printGraph()
graph.dfs("A")
