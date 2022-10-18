n = int(input())
s=[]
for _ in range(n):
    sentence = input()
    if sentence not in s:
        s.append(sentence)
    else:
        pass
s.sort()
s.sort(key=len)
for x in s:
    print(x)