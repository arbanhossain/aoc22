import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return (self.x == other.x and self.y == other.y)

  def __repr__(self):
    return f"Point({self.x}, {self.y})"
  
  def dist(self, point):
    return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

direction_dict = {
  "R": Point(1, 0),
  "L": Point(-1, 0),
  "U": Point(0, 1),
  "D": Point(0, -1)
}


class Knot:
  def __init__(self, pos):
    self.visited = set()
    self.visited.add((0,0))
    self.pos = pos
  
  def move_delta(self, delta):
    self.pos.x += delta.x
    self.pos.y += delta.y
    self.visited.add((self.pos.x, self.pos.y))

class Rope:
  def __init__(self, knot_count):
    self.knots = []
    for _ in range(knot_count):
      self.knots.append(Knot(Point(0,0)))
  
  def evaluate_knot_pos(self, i):
    for a in range(-1,2):
      for b in range(-1,2):
        if Point(self.knots[i-1].pos.x + a, self.knots[i-1].pos.y + b) == self.knots[i].pos:
          return
    

    available_pos = []

    for a in range(-1,2):
      for b in range(-1,2):
        available_pos.append(
          Point(self.knots[i-1].pos.x + a, self.knots[i-1].pos.y + b)
        )

    # For Part 1:
    # available_pos = [
    #   Point(self.knots[i-1].pos.x - 1, self.knots[i-1].pos.y),
    #   Point(self.knots[i-1].pos.x + 1, self.knots[i-1].pos.y),
    #   Point(self.knots[i-1].pos.x, self.knots[i-1].pos.y + 1),
    #   Point(self.knots[i-1].pos.x, self.knots[i-1].pos.y - 1),
    # ]

    d = 10000

    for p in available_pos:
      if p.dist(self.knots[i].pos) < d:
        d = p.dist(self.knots[i].pos)
        point = p
    
    self.knots[i].move_delta(Point(point.x - self.knots[i].pos.x, point.y - self.knots[i].pos.y))
  
  def move_head(self, direction, steps_count):
    for _ in range(steps_count):
      self.knots[0].move_delta(direction_dict[direction])
      for k in range(1, 10):
        self.evaluate_knot_pos(k)
      # print(f"Head: {self.head.pos}, Tail: {self.tail.pos}")
      # input('evaluate next step: ')

with open("input9.txt") as f:
  data = f.read().splitlines()
  data = [[x.split()[0], int(x.split()[1])] for x in data]

ln = 10

rope = Rope(ln)

for direction, steps in data:
  # print(direction, steps)
  rope.move_head(direction=direction, steps_count=steps)

print(len(rope.knots[1].visited),len(rope.knots[9].visited))