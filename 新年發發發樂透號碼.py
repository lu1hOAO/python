import random
lottolist=list()
for i in range(7):
    temp=random.randint(1,49)
    while temp in lottolist:
        temp=random.randint(1,49)
    lottolist.append(temp)
special=lottolist.pop()
print("樂透中獎號碼:",sorted(lottolist))
print("特別獎:",special)