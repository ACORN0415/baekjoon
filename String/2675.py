n = int(input())
for x in range(n):
    answer=''
    count, sentence = input().split()
    for y in sentence:
        answer+=(int(count)*y)
    print(answer)
