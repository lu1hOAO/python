try:
    while True:
        year=int(input())
        if(year%4==0):
            if(year%100==0):
                if(year%400==0):print("a leap year")
                else:print("a normal year")
            else:print("a leap year")
        else:print("a normal year")   
except EOFError:
    pass