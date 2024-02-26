import re
def camel_to_snake(txt):
    string=re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower()
    return string
txt=input()
print(camel_to_snake(txt))