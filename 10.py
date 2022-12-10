with open('input10.txt') as f:
  data = f.read().splitlines()

x = 1

xs = {}

xs[0] = 1

cycle = 0

for instruction in data:
  cycle += 1
  xs[cycle] = x
  if not(instruction.startswith('noop')):
    cycle += 1
    xs[cycle] = x
    x += int(instruction.split()[1])

print(sum(xs[k] * k for k in range(20, 221, 40)))

i = 1

s = []

print(max(xs.keys()))

for i in range(1,241):
  if xs[i] - 1 <= i % 40 -1 <= xs[i] + 1:
    print('#', end='')
  else: print('.', end='')
  if i % 40 == 0:
    print('\n')
