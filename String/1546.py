n = int(input())
maxN = 0
numList = []
sumNum=0
numList = list(map(int, input().split()))
maxN = max(numList)
for idx, x in enumerate(numList):
    numList[idx] = numList[idx]/maxN
    sumNum += numList[idx]
Mean = sumNum/n*100
print(Mean)







# for x in range(n):
#     number = int(input())
#     maxN = max(number, maxN)
#     numList.append(number)
# for idx, x in enumerate(numList):
#     numList[idx] = numList[idx]/maxN
#     sumNum += numList[idx]
# Mean = sumNum/n
# print(Mean)