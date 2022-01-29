while True:
    number=int(input())
    if number==0:
        break
    for i in range (0,number,1):
        if i%7!=0:
            print(i,end=" ")
    print("\n")
