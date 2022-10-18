
# from itertools import combinations
# from operator import itemgetter
# lis=[]
# data = []
# for i in range(1,101):
#     lis.append(i)
# answer = list(combinations(lis, 4))
# for x in answer:
#     x = sorted(x)
# answer.sort(key=itemgetter(3))
# for x in answer:
#     if x[3]**3 ==x[0]**3+x[1]**3+x[2]**3:
#         print("Cube = %d, Triple = (%d,%d,%d)"%(x[3],x[0],x[1],x[2]))

for a in range(5,101):
    for b in range(2,101):
        for c in range(b+1,101):
            for d in range(c+1,101):
                count=d
                if a**3 ==b**3+c**3+d**3:
                    print("Cube = %d, Triple = (%d,%d,%d)"%(a,b,c,d))
                else:
                    continue