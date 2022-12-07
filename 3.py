def priority(char):
  if 65 <= ord(char) <= 90:
    return ord(char) - 38
  elif 97 <= ord(char) <= 122:
    return ord(char) - 96

def findMissingPriority(s):
  half1 = list(s[:len(s)//2])
  half2 = list(s[len(s)//2:])
  for c in half1:
    if c in half2:
      return priority(c)

def findBadgePriority(s1, s2, s3):
  set1 = set(s1)
  set2 = set(s2)
  set3 = set(s3)

  for c in set1:
    if c in set2 and c in set3:
      return priority(c)


if __name__ == '__main__':
  with open('input3.txt') as f:
    data = f.read().split("\n")
  total = 0
  for i in range(0, len(data), 3):
    total += findBadgePriority(data[i], data[i+1], data[i+2])
  print(total)