#!/usr/bin/python3
# import
f = open("apache_logs.txt","r")
f1 = f.readlines()
dicti={}
total = 0
for x in f1:
    responseCode = x.split()[8]
    if responseCode not in dicti:
        dicti[responseCode]=1
    else:
        dicti[responseCode]+=1
    total+=1
dicti = sorted(dicti.items(),key = lambda kv:(kv[1],kv[0]),reverse=True)
for key,value in dicti:
    print(key,round(value/total*100,4))
f.close()