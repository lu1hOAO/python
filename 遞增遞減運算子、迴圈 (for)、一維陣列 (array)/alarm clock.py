while True:
    h1,m1,h2,m2=map(int,input().split(" "))
    if h1==0 and m1==0 and h2==0 and m2==0:
        break
    if h2>h1 and m2>=m1:
        time=(h2-h1)*60+(m2-m1)
    elif h2>h1 and m2<m1:
        time=(h2-h1-1)*60+(m2+60-m1)
    elif h2==h1 and m2>m1:
        time=m2-m1
    elif h2==h1 and m2==m1:
        time=0
    elif h2==h1 and m2<m1:
        time=24*60-(m1-m2)
    elif h2<h1:
        time=(23-h1)*60+(60-m1)+h2*60+m2
    print(time)