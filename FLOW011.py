t=int(input())
pro=1
for i in range(t):
    a=int(input())
    if(a<1500):
        sal=a+0.1*a+.9*a
    else:
        sal=a+500+.98*a
    print(float(sal))
