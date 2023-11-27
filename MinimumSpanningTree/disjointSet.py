
class DisjointSet:
  def __init__(self, vertices): #Time-O(N) Space-O(N)
    self.vertices = vertices
    self.parent = {}
    for v in vertices:
      self.parent[v] = v
    self.rank = dict.fromkeys(vertices, 0)

  def find(self, item): #Time-O(1) Space-O(1)
    if self.parent[item] == item:
      return item
    else:
      return self.find(self.parent[item])
    
  def union(self, x, y): #Time-O(1) Space-O(1)
    xroot = self.find(x)
    yroot = self.find(y)
    if self.rank[xroot]<self.rank[yroot]:
      self.parent[xroot] = yroot
    elif self.rank[xroot]>self.rank[yroot]:
      self.parent[yroot]=xroot
    else:
      self.parent[yroot]=xroot
      self.rank[xroot]+=1

vertices = ["A", "B", "C", "D", "E"]

ds = DisjointSet(vertices)