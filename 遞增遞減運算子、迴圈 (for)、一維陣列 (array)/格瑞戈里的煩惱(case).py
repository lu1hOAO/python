times=int(input())
for i in range(1,times+1):
    year=int(input())
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):print("Case {}: a leap year".format(i))
            else:print("Case {}: a normal year".format(i))
        else:print("Case {}: a leap year".format(i))
    else:print("Case {}: a normal year".format(i))
