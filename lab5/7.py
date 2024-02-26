import re
def snake_to_camel(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))
s=input()
print(snake_to_camel(s))