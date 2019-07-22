n=int(input())
fact=1
for i in range(n):
    number=int(input())
    if(number==0 or number==1):
        print('1')
    else:
        while(number!=0):
            fact=number*fact
            number=number-1
        print(fact)
        fact=1
