class Device:
  def __init__(self):
    self.explorer = {"/":{}}
    self.current_dir = "/"

  def start_of_packet_marker(self, datastream, char_length):
    ln = len(datastream)
    for i in range(ln - char_length):
      sequence = datastream[i:i+char_length]
      # print(list(sequence), set(sequence))
      if sorted(list(sequence)) == sorted(list(set(sequence))):
        return i+char_length
  
  def calculate_dir_size(self, dir):
    size = 0
    for entry in self.explorer[dir]:
      if self.explorer[dir][entry] == "size": continue
      elif self.explorer[dir][entry]["type"] == "file":
        size += self.explorer[dir][entry]["size"]
      else:
        new_dir = dir + entry + "/"
        size += self.calculate_dir_size(new_dir)
    self.explorer[dir]["size"] = size
    return size
  
  def cd(self, to_dir):
    if to_dir == "/":
      self.current_dir = "/"
    elif to_dir == "..":
      current_dir_list = [x for x in self.current_dir.split("/") if x != '']
      current_dir_list.pop()
      if current_dir_list == []: self.current_dir = "/"
      else: self.current_dir =  "/" + "/".join(current_dir_list) + "/"
    else:
      self.current_dir += to_dir + "/"
      if self.current_dir not in self.explorer:
        self.explorer[self.current_dir] = {}
    # print(self.current_dir)
  
  def ls(self, files):
    for file in files:
      size, name = file.split()
      if size == 'dir':
        to_dir = self.current_dir + name + "/"
        if to_dir not in self.explorer: self.explorer[to_dir] = {}
        self.explorer[self.current_dir][name] = {"type": "dir", "size": 0}
      else:
        self.explorer[self.current_dir][name] = {"type": "file", "size": int(size)}

  def process_commands(self, data):
    for command in data:
      cmd, *output = command
      cmd, *args = cmd.split()
      if cmd == 'cd':
        # print (cmd, args)
        self.cd(args[0])
      elif cmd == 'ls':
        self.ls(output)
