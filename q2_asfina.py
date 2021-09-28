n=int(input("enter limit"))


for x in range(n+1):
    temp=x
    i=n-1
    for y in range(0,x):
        print(temp,end=" ")
        temp=temp+i
        i=i-1
    print()
    