n=int(input())
sum=0
for i in range(n):
    number=int(input())
    while(number!=0):
        a=number%10
        sum=sum+a
        number=number//10
    print(sum)
    sum=0
