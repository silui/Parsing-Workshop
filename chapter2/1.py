import re
try:
    my_file_handle=open("example.txt")
except IOError:
        print("File not found or path is incorrect")
finally:
   print("exit")
p=re.compile("[A-Za-z]+")
k=my_file_handle.read()
print(len(p.findall(k)))
