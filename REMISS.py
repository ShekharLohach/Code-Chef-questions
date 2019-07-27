t = int(input())
for i in range(t):
    (a,b) = map(int,input().split())
    if(a>0 and b>0):
        if(a>b):
            min = a
            max = a+b
        else:
            min = b
            max = a + b
        print(min,max)
