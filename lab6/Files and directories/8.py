import os
root=input()
if os.path.exists(root):
    if os.access(root,os.F_OK):
        os.remove(root)