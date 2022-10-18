s = list(map(int, input().split()))
sum=0
for x in s:
    sum +=(x*x)
print(sum%10)