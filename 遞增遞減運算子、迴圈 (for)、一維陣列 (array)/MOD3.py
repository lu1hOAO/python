case_number=int(input())
number1=0;number2=0;number3=0
for i in range(0,case_number):
    sample=int(input())
    if sample%3==0:
       number1+=1
    elif sample%3==1:
         number2+=1
    else:
        number3+=1
print(number1,number2,number3)
