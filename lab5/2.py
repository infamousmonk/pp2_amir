import re
def match(string):
    if re.findall('ab{2,3}', string):
        return 'YES'
    else:
        return 'NO'
s=input()
print(match(s))