def nroot(x,y):
    return x**(1/y)
x=int(input("請輸入被開方的數字："))
y=int(input("請輸入開方數字:"))
result=int(nroot(x,y))
print(x,"開",y,"次方為",result)
