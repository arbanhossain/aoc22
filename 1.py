elves = []

with open('input1a.txt') as f:
  elves = [[int(a) for a in x.split("\n") if a != ''] for x in f.read().split("\n\n")]

result1 = sum((sorted([sum(x) for x in elves]))[-3:])

print(result1)