timeNow = input()
timeThrow = input()
nowT= timeNow.split(":")
throwT = timeThrow.split(":")
waitT = []
for  i,x in enumerate(nowT):
    waitT.append(int(throwT[i])-int(nowT[i]))
for i, x in enumerate(waitT):
    if i > 0:
        if x < 0:
            waitT[i] +=60
            waitT[i-1]-=1
        else:
            pass
    elif i==0:
        if x < 0:
            waitT[i]+=24
        else:
            pass
print("%02d:%02d:%02d"%(waitT[0],waitT[1],waitT[2] ))