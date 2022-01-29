try:
    while True:
        number=int(input())
        s=0
        for i in range(1,number,1):
            if number%i==0:
                s+=i
        if s>number:
            print("盈數")
        elif s==number:
            print("完全數")
        else :
            print("虧數")
except EOFError:
    pass
