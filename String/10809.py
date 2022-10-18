dict = {}
for x in range(ord('A'),ord('Z')+1):
    dict[chr(x)]=-1
s = input().upper()
for idx,x in enumerate(s):
    if dict[x] != -1 :
        pass
    elif x in dict:
        dict[x] = idx

for x in dict.values():
    print(x, end=' ')
