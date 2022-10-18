alpha_NUM = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
sentence = input()
arr = []
for x in sentence:
    s = ord(x)-ord('A')
    arr.append(alpha_NUM[s])
print(sum(arr))
sumN = sum(arr)%10 
if sumN%2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")