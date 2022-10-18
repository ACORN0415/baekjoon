strC = []
strL = []
answer = ""
for x in range(5):
    s = input()
    strC.append(len(s))
    strL.append(s)
count = 0
flag = True
maxN = max(strC)
while flag:
    for x in strL:
        if len(x)>count:
            answer += x[count]
        elif count>maxN:
            flag = False
            break
        else:
            pass

    count+=1
print(answer)