import re
def func(txt):
    if re.findall('([A-Z]{1})+[a-z]*', txt):
        return 'YES'
    else:
        return 'NO'
s=input()
print(func(s))