import sys
T = int(sys.stdin.readline())
for _ in range(T):
    count=0
    n,m = map(int, sys.stdin.readline().split())
    for x in range(n,m+1):
        count+=str(x).count('0')
    print(count)