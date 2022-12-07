SCORES = {
  # [win, lose, draw]
  "A": {"Z": 2,"X": 3, "Y": 1},
  "B": {"Z": 3,"X": 1, "Y": 2},
  "C": {"Z": 1,"X": 2, "Y": 3}
}

WIN = {
  "X": 0,
  "Y": 3,
  "Z": 6
}


def solve(data):
  total = 0
  for round in data:
    for key, value in round.items():
      if WIN[key]["win"] == value:
        outcome = 6
      elif WIN[key]["draw"] == value:
        outcome = 3
      else:
        outcome = 0
      total += outcome + SCORES[value]
  return total

def solve2(data):
  total = 0
  for round in data:
    for key, value in round.items():
      total += SCORES[key][value] + WIN[value]
  return total

with open('input2.txt') as f:
  lines = f.read().split("\n")
  data = [{x: y} for x, y in [line.split() for line in lines]]

print(solve2(data))