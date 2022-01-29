number=int(input())
i=2
result=""
while number>1:
    if number %i==0: 
        if result!="":
            result+=" * "
        power=1
        number/=i
        while number%i==0:
             number/=i
             power+=1
        if power>1:
            result+=str(i)+"^"+str(power)
        elif power==1:
            result+=str(i)
    i+=1
print(result)