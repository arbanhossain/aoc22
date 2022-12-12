class Node:
  def __init__(self, height: str, node_type=None, cost=float('inf')):
    
    if height == 'S':
      height = 'a'
      # cost = 0 # part 1
      node_type = 'S'
    if height == 'E':
      height = 'z'
      node_type = 'E'
      cost = 0 # part 2

    self.cost = cost
    self.height: int = ord(height)
    self.node_type = node_type
  
  def __repr__(self):
    return f'Node(Height: {self.height}, Cost: {self.cost}, Node Type: {self.node_type})'

def get_neighbors(i, j, nodes: list):
  neighbors = []
  if i > 0:
    neighbors.append(nodes[i-1][j])
  if i < len(nodes)-1:
    neighbors.append(nodes[i+1][j])
  if j > 0:
    neighbors.append(nodes[i][j-1])
  if j < len(nodes[i])-1:
    neighbors.append(nodes[i][j+1])
  return neighbors

def get_unvisited_with_lowest_cost(visited_set, nodes):
  lowest_cost = float('inf')
  lowest_cost_node = None
  a, b = 0, 0
  for i in range(len(nodes)):
    for j in range(len(nodes[i])):
      node = nodes[i][j]
      if node not in visited_set:
        if node.cost < lowest_cost:
          lowest_cost = node.cost
          lowest_cost_node = node
          a, b = i, j
  return lowest_cost_node, a, b

with open('input12.txt') as f:
  data = f.read().splitlines()

nodes = []
for line in data:
  temp = []
  for c in list(line):
    temp.append(Node(c))
  nodes.append(temp)

visited = set()

i, j = 0, 0

while True:
  node, i, j = get_unvisited_with_lowest_cost(visited, nodes)
  visited.add(node)
  neighbors = get_neighbors(i, j, nodes)
  for neighbor in neighbors:
    if node.height - neighbor.height <= 1:
      if neighbor.cost > node.cost + 1:
        neighbor.cost = node.cost + 1
  if node.height == 97:
    break

print(nodes[i][j])