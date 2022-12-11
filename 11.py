import re
from pprint import pprint as pp
import math
import numpy as np

p = r"""Monkey (.*):
  Starting items: (.*)
  Operation: (.*)
  Test: divisible by (.*)
    If true: throw to monkey (.*)
    If false: throw to monkey (.*)"""

with open('input11.txt') as f:
  data = f.read().split("\n\n")

monkeys = {}

for inp in data:
  x = re.match(p, inp)
  curr_monkey, items, operation, divisible_by, if_true, if_false = x.groups()

  monkeys[curr_monkey] = {
    "items": [int(x) for x in items.split(", ")],
    "operation": operation,
    "divisible_by": int(divisible_by),
    "if_true": if_true,
    "if_false": if_false,
    "inspected": 0
  }

# pp(monkeys)

total = 1

for monkey in monkeys:
  total *= monkeys[monkey]["divisible_by"]

for _ in range(10000):
  for monkey in monkeys:
    for item in monkeys[monkey]["items"]:
      monkeys[monkey]["inspected"] += 1
      new = 0
      old = int(item)
      new = eval(monkeys[monkey]["operation"].split(' = ')[1])
      # new = math.floor(new/3) # for part 1
      new = new % total # for part 2
      if new % monkeys[monkey]["divisible_by"] == 0:
        monkeys[monkeys[monkey]["if_true"]]["items"].append(new)
      else:
        monkeys[monkeys[monkey]["if_false"]]["items"].append(new)
    monkeys[monkey]["items"] = []

# sort monkeys by inspected in reverse
monkeys = dict(sorted(monkeys.items(), key=lambda item: item[1]["inspected"], reverse=True))

active_monkeys = 2
mb = 1

for monkey in monkeys:
  if active_monkeys == 0:
    break
  else: mb *= monkeys[monkey]["inspected"]
  active_monkeys -= 1

print(mb)