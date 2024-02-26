import re
def func(string):
    if re.findall('[a-z]_\B',string):
        return "YES"
    else:
        return "NO"
s=input()
print(func(s))