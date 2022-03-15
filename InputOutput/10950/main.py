T = int(input())
for x in range(0,T):
    number = input()
    a = number.split(' ')[0]
    b = number.split(' ')[1]
    c = int(a)+int(b)
    print(c)