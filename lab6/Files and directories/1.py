import os
from fnmatch import fnmatch
print('1-Show directories')
print('2-Show all files')
print('3-Show all')
option=int(input())
root=input()
if option==1:
    for folder in os.listdir(root) :
        if os.path.isdir(root+'\\'+folder):
            print(folder)
if option==2:
    for name in os.listdir(root):
        if os.path.isfile(root+'\\'+name):
            print(name)
if option==3:
    for x in os.listdir(root):
        print(x)