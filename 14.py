def add_to_rocks(p1, p2, rocks):
  if p1[0] == p2[0]:
    for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
      rocks.add((p1[0], y))
  elif p1[1] == p2[1]:
    for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
      rocks.add((x, p1[1]))
  else:
    print('Error: not a horizontal or vertical line')

with open('input14.txt') as f:
  data = f.read().splitlines()
  data = [x.split(' -> ') for x in data]

# print(data)

rocks = set()
sands = set()

for structure in data:
  for point in range(len(structure) - 1):
    p1 = [int(x) for x in structure[point].split(',')]
    p2 = [int(x) for x in structure[point+1].split(',')]
    add_to_rocks(p1, p2, rocks)

# get the max y coordinate in rocks
ground_y = max([x[1] for x in rocks]) + 2
add_to_rocks([0, ground_y], [1000, ground_y], rocks)

sand = (500,0)
rest = 0

while True:
  x, y = sand
  # check if there is any point in sands or rocks with the same horizontal coordinate
  # if not, then we have reached the abyss
  if not any([s[0] == x for s in sands]) and not any([s[0] == x for s in rocks]):
    break
  if (x, y+1) not in rocks and (x, y+1) not in sands:
    sand = (x, y+1)
  elif (x-1, y+1) not in rocks and (x-1, y+1) not in sands:
    sand = (x-1, y+1)
  elif (x+1, y+1) not in rocks and (x+1, y+1) not in sands:
    sand = (x+1, y+1)
  else:
    if sand == (500, 0):
      break
    sands.add((x, y))
    sand = (500, 0)
    rest += 1
    print(f"At rest: {rest}")

print(rest+1)
