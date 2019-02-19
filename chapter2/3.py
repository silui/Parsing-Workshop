import re,sys
try:
    my_file_handle=open("example.txt")
except IOError:
        print("File not found or path is incorrect")
k='a'
while k:
  k=my_file_handle.readline()
  if sys.argv[1] in k:
    print(k)
