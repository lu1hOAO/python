print("******************************************************************")
print("遊戲說明：")
print("1A2B是一個益智小遊戲輸入多個不重複的數字，和電腦隨機跑出的數字做比較")
print("如果數字對位置對就是A，如果只有數字對是B喔!")
print("小恐龍祝你遊戲愉快")
print("                \||/")
print("                |  @___oo")
print("      /\  /\   / (__,,,,|")
print("     ) /^\) ^\/ _)")
print("     )   /^\/   _)")
print("     )   _ /  / _)")
print(" /\  )/\/ ||  | )_)")
print("<  >      |(,,) )__)")
print(" ||      /    \)___)\\")
print(" | \____(      )___) )___")
print("  \______(_______;;; __;;;")
print("*******************************************************************")
import random
ans='y'
while ans=='y' or ans=='Y':
    guessnum=int(input("請問你要猜測幾個數字的密碼:（最多十個）"))
    pwd=random.sample(range(0,10),guessnum)
    #print(pwd)
    A=0
    B=0
    while A!=guessnum:
        num=input("請輸入"+str(guessnum)+"個數字(數字不重複)：")
        if len(num)!=guessnum or len(set(num))!=guessnum:
            continue
        test=list(map(int,list(num)))
        A=0
        B=0
        for i in range(0,guessnum):
            if test[i] in pwd:
                if i==pwd.index(test[i]):
                    A+=1
                else:
                    B+=1
        print(num,":",A,"A",B,"B",sep=(""))
    print("你猜對了,密碼是",num)
    print("                \||/")
    print("                |  @___oo")
    print("      /\  /\   / (__,,,,|")
    print("     ) /^\) ^\/ _)")
    print("     )   /^\/   _)")
    print("     )   _ /  / _)")
    print(" /\  )/\/ ||  | )_)")
    print("<  >      |(,,) )__)")
    print(" ||      /    \)___)\\")
    print(" | \____(      )___) )___")
    print("  \______(_______;;; __;;;")
    print("你還要再玩嗎？(y/n)")
    ans=chr(input())
print("byebye~下次再來喔")
