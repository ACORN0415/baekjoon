import sys
T = int(sys.stdin.readline())
def checkPalindrome(s):
    if len(s)%2==0:
        s2 = s[len(s)//2::]
        s2 = s2[::-1]
        if s[0:len(s)//2] ==s2:
            return 1
        else:
            return 0
    else:
        s2 = s[len(s)//2+1::]
        s2 = s2[::-1]
        if s[0:len(s)//2] ==s2:
            return 1
        else:
            return 0
for _ in range(T):
    s = sys.stdin.readline().rstrip()
    if checkPalindrome(s):
        print(0)
    else:
        for idx in range(len(s)):
            newstr = s[:idx]+s[idx+1:]
            if checkPalindrome(newstr):
                print(1)
                break
        else:
            print(2)
