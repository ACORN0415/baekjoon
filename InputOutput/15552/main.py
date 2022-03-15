import sys

T = int(sys.stdin.readline().rstrip())
5
for x in range(0,T):
    a,b =map(int, sys.stdin.readline().split())
    print(a+b)