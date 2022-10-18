vowel =['e','o','a','i','u']
def check(s):
    flag =0
    for idx, x in enumerate(s):    
        if x in vowel:
            flag =1
            if idx+1<len(s):
                if x!='e'and x!='o' and s[idx+1]== x:
                    return 0
            if idx+2<len(s): 
                if s[idx+1]in vowel and s[idx+2] in vowel:
                    return 0
        elif x not in vowel:
            if idx+1<len(s):
                if  s[idx+1]== x:
                    return 0
            if idx+2<len(s):
                if s[idx+1] not in vowel and  s[idx+2] not in vowel:
                    return 0
           
    return flag

while True:
    sentence = input()
    if sentence == "end":
        break
    if check(sentence) == 1:
        print("<%s> is acceptable."%sentence)
    else:
        print("<%s> is not acceptable."%sentence)