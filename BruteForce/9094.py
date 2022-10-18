import sys
T = int(input())
for _ in range(T):
    count =0
    n,m = map(int, sys.stdin.readline().split())
    for a in range(1,n):
        for b in range(a+1,n):
            if ((a*a+b*b+m)/(a*b)).is_integer():
                count+=1
    print(count)