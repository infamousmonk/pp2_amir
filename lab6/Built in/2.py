s=input()
cnt_1=0
cnt_2=0
for i in s:
    if i.isupper():
        cnt_1+=1
    if i.islower():
        cnt_2+=1
print('Upper'+' '+ str(cnt_1))
print('Lower'+' '+ str(cnt_2))