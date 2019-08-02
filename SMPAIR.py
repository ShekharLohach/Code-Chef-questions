t=int(input())
for i in range(t):
    n=int(input())
    a = list(map(int, input().split()))
    sort=sorted(a)
    sum=sort[0]+sort[1]
    print(sum)
