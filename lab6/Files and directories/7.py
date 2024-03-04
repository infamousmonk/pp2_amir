import time
import os
f=open('test.txt','r')
d=open('res.txt','w')
for i in f:
    d.write(i)