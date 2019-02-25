import pyshark
cap = pyshark.FileCapture('http.cap')

first = cap[0].sniff_time

for packet in cap:
  print(packet.sniff_time-first)
  first = packet.sniff_time


# for i in range(len(cap)):
#   print(cap[i])