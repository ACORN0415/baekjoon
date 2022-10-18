def checker(s):
    dic = {}
    for idx ,x in enumerate(s):
        if x not in dic:
            dic[x] = 1
        elif x in dic and s[idx-1] !=x:
            return False
    return True
n = int(input())
count =0
for x in range(n):
    s = input()
    if checker(s)==True:
        count+=1
    else:
        pass
print(count)
    

