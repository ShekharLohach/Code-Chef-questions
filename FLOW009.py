t=int(input())
for i in range(t):
    (a,b)=map(int,input().split())
    if(a>1000):
        price=float(a*b*0.9)
    else:
        price=float(a*b)
    print(format(price,'.6f'))
