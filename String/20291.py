n = int(input())
dic={}
for x in range(n):
    s=input().split('.')[1]
    if s in dic:
        dic[s] +=1
    else:
        dic[s] = 1
sorted_dic = sorted(dic)
for x in sorted_dic:
    print("%s %d"%(x,dic[x]))