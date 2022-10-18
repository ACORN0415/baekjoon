import sys
N,K = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))
maxN = -100
for x in range(N):
    if x+K <=N:
        maxN = max(sum(numlist[x:x+K]),maxN)
        print('x',x,'x+K',x+K,sum(numlist[x:x+K]))
print(maxN)