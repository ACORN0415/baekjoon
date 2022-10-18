n1,n2 = map(int,input().split())
noListen = set()
noLook = set()
for _ in range(n1):
    noListen.add(input())
for _ in range(n2):
    noLook.add(input())
addSet = noLook&noListen
addSet = list(addSet)
addSet.sort()
print(len(addSet))
for x in addSet:
    print(x)