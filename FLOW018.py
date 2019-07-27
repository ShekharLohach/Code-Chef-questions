t=int(input())
suma=1
for i in range(t):
    n=int(input())
    if(n==0 or n==1):
        print("1")
    else:
        while(n!=0):
            suma=suma*n
            n=n-1
        print(suma)
        suma=1
