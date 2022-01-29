case_num=int(input())
for i in range(0,case_num):
    people=int(input())
    sum=0
    for j in range(0,people):
        square,animal,level=map(int,input().split(" "))
        sum+=square*level
    print(sum)
