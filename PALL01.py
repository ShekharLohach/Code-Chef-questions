t=int(input())
reverse=''
for i in range(t):
    a =(input())
    for i in range(1,len(a)+1):
        reverse=reverse+a[-i]
    if(a==reverse):
        print("wins")
    else:
        print("losses")
    reverse=""
