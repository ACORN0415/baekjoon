s=[]
for x in range(10):
    num = int(input())%42
    if num in s:
        pass
    else:
        s.append(num)
print(len(s))
