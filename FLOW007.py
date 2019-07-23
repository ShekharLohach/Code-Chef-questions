n=int(input())
sum=""
for i in range(n):
    b=input()
    lenght=len(b)+1
    for i in range(1,lenght):
        count=b[-i]
        sum=sum+count
    print(int(sum))
    sum=""
