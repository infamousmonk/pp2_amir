import os
import time
name=[]
for x in range(65,91):
    name.append(chr(x)+'.txt')
for x in range(0,26):
    open(name[x],'a').close()
time.sleep(5)
for x in range(65,91):
    os.remove(f"{chr(x)}.txt")