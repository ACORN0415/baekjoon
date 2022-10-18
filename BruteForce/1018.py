N, M = map(int,input().split())
count =0
sentence = []
for x in range(N):
    sentence.append(input())
for idx1,x in enumerate(sentence):
    for idx2,y in enumerate(x):
        if sentence[0][0] =='W':
            if idx1 %2 == 0:
                if idx2 %2 == 0:
                    if y!='W':
                        count +=1
                    else:
                        pass
                else:
                    if y!='B':
                        count +=1
                    else:
                        pass
            else:
                if idx2 %2 == 0:
                    if y!='B':
                        count +=1
                    else:
                        pass
                else:
                    if y!='W':
                        count +=1
                    else:
                        pass
        else:
            if idx1 %2 == 0:
                if idx2 %2 == 0:
                    if y!='B':
                        count +=1
                    else:
                        pass
                else:
                    if y!='W':
                        count +=1
                    else:
                        pass
            else:
                if idx2 %2 == 0:
                    if y!='W':
                        count +=1
                    else:
                        pass
                else:
                    if y!='B':
                        count +=1
                    else:
                        pass
            
print(count)

    