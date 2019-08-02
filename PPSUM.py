t=int(input())
sum=0
for i in range(t):
    (d,n)=map(int,input().split())
    for i in range(d):
        for j in range(1, n+1):
            sum=sum+j
        n = sum
        sum=0

    print(n)

    sum=0
