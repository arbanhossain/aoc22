from device import Device
from pprint import pprint as pp

d = Device()

with open('input7.txt') as f:
  data = [[a.strip() for a in x.split("\n") if a != ''] for x in f.read().split("$") if x != '']


# for lines in data:
#   if lines[0] == '$':
#     command = " ".join(lines.split()[1:])
#     cmd, *args = command.split()
#     if cmd == 'cd':
#       d.cd(args[0])
#     elif cmd == 'ls':

d.process_commands(data)
d.calculate_dir_size("/")

dirs = [{"dir": x, "size": d.explorer[x]["size"]} for x in d.explorer]

dirs.sort(key=lambda x: x["size"])

required = 30000000 - (70000000 - d.explorer["/"]["size"])

for item in dirs:
  if item["size"] > required:
    print(item)
    break