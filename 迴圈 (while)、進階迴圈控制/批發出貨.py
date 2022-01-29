base=int(input())
package=list(map(int,input().split()))
i=0
while package[i]!=0:
    if package[i]%base==0:
        res=package[i]//base
        print(res)
    else:
        res=base*((package[i]//base)+1)-package[i]
        print(res)
    i+=1