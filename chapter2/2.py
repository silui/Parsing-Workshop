import re
try:
    my_file_handle=open("example.txt")
except IOError:
        print("File not found or path is incorrect")
finally:
   print("exit")
p=re.compile("[0-9]+")
k=my_file_handle.read()
newList = list(map(int,p.findall(k)))
print(sum(newList))
