num = int(input())
for x in range(num):
    dict = {}
    sample = input()
    for y in sample:
        if y == " ":
            continue
        if y in dict:
            dict[y] += 1
        elif y not in dict:
            dict[y] = 1
    sorted_dict = sorted(dict.items(),key=lambda x: x[1], reverse=True)

    if len(sorted_dict) == 1:
        print(sorted_dict[0][0])
    elif sorted_dict[0][1] != sorted_dict[1][1]:
        print(sorted_dict[0][0])
    else:
        print('?')