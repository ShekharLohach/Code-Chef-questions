n=int(input())
list=[]
for i in range(n):
    number=int(input())
    list.append(number)

list.sort()
for i in list:
    print(i)
