count =0
maxN =0
for x in range(9):
    n = int(input())
    maxN = max(n,maxN)

    if maxN !=n:
        continue
    else:
        count = x+1
print(maxN)
print(count)