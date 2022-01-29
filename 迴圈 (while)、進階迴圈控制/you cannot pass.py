try:
    while True:
        line=list(map(int,input().split()))
        total=sum(line)-line[0]
        average=total/line[0]
        if average>59:
            print("no")
        else:
            print("yes")
except EOFError:
    pass