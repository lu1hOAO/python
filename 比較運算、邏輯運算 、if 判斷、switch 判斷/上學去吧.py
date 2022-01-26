h,m=map(int,input().split(" "))
if(h<7):
    print("Off School")
    exit 
elif(h==7):
    if(m<30):
        print("Off School")
        exit
    else:
        print("At School")
        exit
elif(7<h<17):
    print("At School")
    exit
elif(h>=17):
    print("Off School")
    exit