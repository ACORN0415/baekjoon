while True:
    try:
        sentence= input()
        s,t = sentence.split()
        if s in t:
            print("Yes")
        else:
            count = len(s)
            for x in s:
                for y in t:
                    if x!=y:
                        t=t[1:]
                    else:
                        t=t[1:]
                        count-=1
                        break
                if count==0:
                    print('Yes')
            if count>0:
                print('No')
    except EOFError:
        break