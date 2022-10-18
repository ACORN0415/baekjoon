s=input()
num1 = []
num2 = []
for idx,x in enumerate(s):
    if x =='<':
       num1.append(idx)
    if x == '>':
        num1.append(idx)
