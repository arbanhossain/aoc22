import functools
from pprint import pprint as pp

LIST = type([])
INT = type(3)

def comp(left, right):
  if type(left) == LIST and type(right) == LIST:
    i = 0
    while True:
      left_over = i >= len(left)
      right_over = i >= len(right)
      if left_over and not right_over: return True
      if right_over and not left_over: return False
      if left_over and right_over: return None
      res = comp(left[i], right[i])
      if res != None: return res
      i += 1
  
  elif type(left) != type(right):
    if type(left) == INT: return comp(list([left]), right)
    elif type(right) == INT: return comp(left, list([right]))
  
  
  elif type(left) == INT and type(right) == INT:
    if left < right: return True
    elif left > right: return False
    else: return None

def cmpkey(left, right):
  res = comp(left, right)
  if res == None: return 0
  elif res: return 1
  else: return -1

with open('input13.txt') as f:
  data = f.read().split("\n\n")

# c = 0

# for i in range(len(data)):
#   pair = data[i]
#   pair = pair.split("\n")
#   left = eval(pair[0])
#   right = eval(pair[1])
#   if comp(left, right): c += i+1

# print(c)

total = []

for pair in data:
  pair = pair.split("\n")
  left = eval(pair[0])
  right = eval(pair[1])
  total.append(left)
  total.append(right)

total.append([[2]])
total.append([[6]])

total = sorted(total, key=functools.cmp_to_key(cmpkey), reverse=True)
# pp(total)

pp((total.index([[2]]) + 1) * (total.index([[6]]) + 1))