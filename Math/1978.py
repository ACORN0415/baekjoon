def is_prime_number(x):
    if x>1:
        for i in range(2, x):
            if x % i == 0:
                return False
    else:
        return False 
    return True 
count =0
n= int(input())
numL = list(map(int, input().split()))
for x in numL:
    if is_prime_number(x) == True:
        count += 1
    else:
        continue
print(count)