n=int(input())
count=0
for i in range(n):
    b=(input())
    for j in b:
        if(j=='4'):
            count+=1
    print(count)
    count=0
