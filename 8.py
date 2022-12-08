def is_visible(i, j, data):
  ln  = len(data)
  elem = data[i][j]

  # first check the row , i constant
  neighbors = [data[i][k] for k in range(j)]
  if elem > max(neighbors): return True
  
  neighbors = [data[i][k] for k in range(j+1, ln)]
  if elem > max(neighbors): return True
  
  neighbors = [data[k][j] for k in range(i)]
  if elem > max(neighbors): return True
  
  neighbors = [data[k][j] for k in range(i+1, ln)]
  if elem > max(neighbors): return True
  
  return False

def score_for_tree(i, j, data):
  ln  = len(data)
  elem = data[i][j]

  score = 1

  # left
  trees = 0
  for k in reversed(list(range(j))):
    trees += 1
    if elem > data[i][k]:
      pass
    else:
      break

  score *= max(1,trees)

  trees = 0
  for k in (list(range(j+1, ln))):
    trees += 1
    if elem > data[i][k]:
      pass
    else:
      break

  score *= max(1,trees)

  trees = 0
  for k in reversed(list(range(i))):
    trees += 1
    if elem > data[k][j]:
      pass
    else:
      break
  
  score *= max(1,trees)

  trees = 0
  for k in (list(range(i+1, ln))):
    trees += 1
    if elem > data[k][j]:
      pass
    else:
      break
  
  score *= max(1,trees)

  return score


with open('8input.txt') as f:
  data = [[int(x) for x in list(d)] for d in f.read().split("\n")]

# print(data)

ln = len(data)

total = 0

score = 0

for i in range(1, ln-1):
  for j in range(1, ln-1):
    if is_visible(i, j, data):
      total += 1

print(total + 4*(ln-1))

for i in range(1,ln-1):
  for j in range(1,ln-1):
    score = max(score, score_for_tree(i, j, data))

print(score)