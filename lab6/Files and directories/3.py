import os
path=input()
if os.access(path,os.F_OK):
    for folder in os.listdir(path):
        if os.path.isdir(path):
            print(folder)
    for file in os.listdir(path):
        if os.path.isfile(path):
            print(file)