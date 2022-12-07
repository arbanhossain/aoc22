from device import Device

with open('input6.txt') as f:
  buff = f.read()

d = Device()

print(d.start_of_packet_marker(buff, 14))