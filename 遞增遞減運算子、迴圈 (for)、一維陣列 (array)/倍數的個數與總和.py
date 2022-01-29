start=int(input("請輸入起始值:"))
end=int(input("請輸入結束值:"))
num=0
num_sum=0
for i in range(start,end+1,1):
    if i%7==0 or i%11==0:
        num+=1
        num_sum+=i
        print("{:<4}".format(i),end=" ")
        if num%10==0:
            print("\n")
print("\n")
print("總數共有",num,"個")
print("數字總合為:",num_sum)
        

