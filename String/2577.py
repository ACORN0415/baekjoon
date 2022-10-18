dict = {}
s=[]
mul = 1
for x in range(10):
    dict[str(x)]=0

for x in range(3):
    s.append(int(input()))
for x in range(3):
    mul*=s[x]
for x in str(mul):
    if x in dict:
        dict[x] += 1

for x in dict:
    print(dict[x])