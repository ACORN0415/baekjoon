sent1 = input()
sent2 = input()
sent3 = ''
for x in sent1:
    if not x.isalpha():
        continue
    else:
        sent3 += x
if sent2 in sent3:
    print(1)
else:
    print(0)