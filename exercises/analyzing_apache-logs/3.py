#!/usr/bin/python3
import re
f = open("apache_logs.txt","r")
f1 = f.readlines()
dicti={}
total = 0
for x in f1:
    # regex = re.compile('\[(\d+\/.+\/\d{4})')
    match = re.search('\[(\d+\/.+\/\d{4}):',x)
    if(match):
        target = match.group(1)
        total+=1
        if target not in dicti:
            dicti[target] = True
print("average request per day = "+str(total/len(dicti)))
    




#     if responseCode not in dicti:
#         dicti[responseCode]=1
#     else:
#         dicti[responseCode]+=1
# dicti = sorted(dicti.items(),key = lambda kv:(kv[1],kv[0]),reverse=True)
# for key,value in dicti:
#     print(key,value)
# f.close()



