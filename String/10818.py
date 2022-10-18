n=int(input())
s = list(map(int, input().split()))
maxN = -1000000
minN = 1000000
for x in s:
    maxN = max(maxN, x)
    minN = min(minN, x)
print("%d %d" %(minN, maxN))