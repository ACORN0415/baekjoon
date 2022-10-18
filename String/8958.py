n = int(input())

for x in range(n):
    s = input()
    count =2
    sumN =0
    for idx, y in enumerate(s):
        if y == 'O':
            if idx>0 and s[idx-1] == 'O':
                sumN += count
                count += 1
            else:
                sumN += 1
                count = 2
        else:
            pass
    print(sumN)
