import os
path=input()
if os.path.exists(path):
    print('Path exists')
else:
    print("Path doesn't exists")
if os.access(path,os.R_OK):
    print('File is readable')
else:
    print("File isn't readable")
if os.access(path, os.W_OK):
    print('File is writable')
else:
    print("File isn't writable")
if os.access(path, os.X_OK):
    print('File is executable')
else:
    print("File isn't executable")