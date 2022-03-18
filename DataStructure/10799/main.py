import sys
def input():
    return sys.stdin.readline().rstrip()
stack = list(input())
answer = []
isAnswer = []
Rcount = 0
Lcount = 0
IsRazer =0
answer1 =0

for x in range(len(stack)):
    if stack[-1] == ')':
        stack.pop()
        if stack[-1] == '(':
            IsRazer +=1
        else:
            isAnswer.append(1)
            answer.append(0)
            Rcount+=1
    elif stack[-1] == '(':
        stack.pop()
        if IsRazer>0 and Rcount >0:
            for y in range(len(answer)):
                if isAnswer[y]>0:
                    answer[y]+=1
            IsRazer = 0
        else:
            Lcount+=1
            isAnswer[-1]= 0
            if Rcount ==Lcount:
                Rcount =0
                Lcount =0
               
for z in range(len(answer)):
    answer1 += answer[z]
answer1+=len(answer)
print(answer1)
'''



'''