import re
def func(txt):
    if re.findall('^a(.+)b$', txt):
        return 'YES'
    else:
        return 'NO'
s=input()
print(func(s))