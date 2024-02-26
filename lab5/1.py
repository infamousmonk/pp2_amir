import re
def match(string):
    if re.findall('ab*', string):
        return 'YES'
    else:
        return 'NO'
s=input()
print(match(s))