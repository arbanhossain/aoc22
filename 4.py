def getRange(s):
  l, r = [int(x) for x in s.split("-")]
  return set(range(l, r+1))

if __name__ == "__main__":
  with open('input4.txt') as f:
    data = [[getRange(a), getRange(b)] for a, b in [x.split(",") for x in f.read().split("\n")]]
  
  total = 0
  overlap = 0
  for a, b in data:
    if len(a.intersection(b)) > 0:
      overlap += 1
    if a.issubset(b) or b.issubset(a):
      total += 1
  print(total, overlap)