seat=int(input())
if seat<=2500:
    region=1
    line=(seat+24)//25
    dot=(seat+24)%25+1
elif 2500<seat<=7500:
    region=2
    seat-=2500
    line=(seat+49)//50
    dot=(seat+49)%50+1
else:
    region=3
    seat-=7500
    line=(seat+24)//25
    dot=(seat+24)%25+1
print(region,line,dot)


