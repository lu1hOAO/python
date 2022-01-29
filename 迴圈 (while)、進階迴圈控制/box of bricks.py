try:
    case_number=1
    while True:
        wallnumber=int(input())
        if wallnumber==0:
            break
        line=list(map(int,input().split()))
        height=sum(line)//wallnumber
        time=0
        for i in range(0,len(line),1):
            if line[i]>height:
                time+=line[i]-height
        print("Set #{}".format(case_number))
        print("The minimum number of moves is {}.".format(time))
        case_number+=1
except EOFError:
    pass