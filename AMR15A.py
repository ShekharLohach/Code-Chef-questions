t=int(input())
odd=0
even=0
li=list(map(int,input().split()))
for i in li:
    if(i%2==0):
        even+=1
    else:
        odd+=1

if(even>odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
