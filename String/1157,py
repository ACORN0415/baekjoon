s = input()
s1 = s.upper()
dict = {}
for y in s1:
    if y in dict:
        dict[y] += 1
    else:
        dict[y] = 1
sorted_dict = sorted(dict.items(),key=lambda x: x[1], reverse=True)

if len(sorted_dict) == 1:
    print(sorted_dict[0][0])
elif sorted_dict[0][1] != sorted_dict[1][1]:
    print(sorted_dict[0][0])
else:
    print('?')
