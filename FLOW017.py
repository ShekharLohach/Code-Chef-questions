t=int(input())
for i in range(t):
    (a, b,c) = map(int, input().split())
    if(a<b<c or c<b<a ):
        print(b)
    elif(b<a<c or c<a<b):
        print(a)
    else:
        print(c)
