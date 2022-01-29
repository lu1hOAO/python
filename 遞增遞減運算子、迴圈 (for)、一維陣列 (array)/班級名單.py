student=int(input())
a,b,c=map(int,input().split(" "))
for i in range (student,0,-1):
    if i!=a and i!=b and i!=c:
        print("No.",i)