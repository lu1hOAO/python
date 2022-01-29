def f91(N):

    if N<=100:
      return f91(f91(N+11))

    elif N>=101:
      return N-10
      
while True:
    n=int(input())
    if n==0:
        break
    print("f91({}) = {}".format(n,f91(n)))
   
