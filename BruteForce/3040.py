from itertools import permutations
import sys
s = []
data = []
for _ in range(9):
    s.append(int(sys.stdin.readline().rstrip()))
answer = list(permutations(s, 7))
for x in answer:
    if sum(x)==100:

        data = sorted(list(x))
        # print(data)
        break
for x in data:
    print(x)