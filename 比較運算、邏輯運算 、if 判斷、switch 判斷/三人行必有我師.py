a,b,c=map(int,input().split(" "))
max=0
if a>b: max=a
else:max=b
if max<c:max=c
print(max)