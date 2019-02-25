import pyshark
cap = pyshark.FileCapture('http.cap')

# print("Source" in cap[0])

# print(dir(cap)) # Prints all the fields that can be accessed

for packet in cap:          # Loops through every packet captured
  if "65.208.228.223" in packet.ip.src or "65.208.228.223" in packet.ip.dst:
      print("-------------------------------")
      print(packet)
    # print(packet)
#   print(packet)  # Prints out the timestamp of the packet