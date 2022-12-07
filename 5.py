class Stack:
  def __init__(self):
    self.itemList = []
    self.ln = 0
  
  def push(self, item):
    self.itemList.append(item)
    self.ln += 1

  def pop(self):
    self.ln -= 1
    if self.ln < 0:
      self.ln = 0
    return self.itemList.pop()
  
  def seeLast(self):
    return self.itemList[len(self.itemList)-1]
  
  def __repr__(self):
    return str(self.itemList)


if __name__ == "__main__":
  with open('input5.txt') as f:
    stack, moves = [x.split("\n") for x in f.read().split("\n\n")]
  
  stackCount = (len(stack[0])//4) + 1
  crate_stacks = []
  for _ in range(stackCount):
    crate_stacks.append(Stack())
  for x in reversed(stack):
    if x[2] == '1': continue
    l = list(x)
    for i in range(0, len(l), 4):
      if(l[i] == '['):
        crate_stacks[i//4].push(l[i+1])
  moves = [[int(x) for x in move.split() if x.isdigit()] for move in moves]
  # print(crate_stacks)
  for move in moves:
    crate_count, stack_from, stack_to = move
    crate_stacks[stack_to-1].itemList += crate_stacks[stack_from-1].itemList[-crate_count:]
    crate_stacks[stack_from-1].itemList = crate_stacks[stack_from-1].itemList[:-crate_count] 
    # print(crate_stacks)
  print("".join([s.seeLast() for s in crate_stacks]))