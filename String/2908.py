s = input().split()
ascount =1
decount = 8
if int(s[0]) == ascount:
    for x in s:
        if int(x) == ascount:
            ascount+=1
            if int(x) == decount:
                print("ascending")
        else:
            print("mixed")
            break
elif int(s[0]) == decount:
    for x in s:
        if int(x) ==decount:
            decount-=1
            if int(x) == ascount:
                print("descending")
        else:
            print("mixed")
            break
else:
    print("mixed")
    