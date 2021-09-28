n=int(input("enter limit"))

for x in range(n,0,-1):
    for y in range(2*n-1):
        if(y>=x and y<2*n-x-1):
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()
for x in range(n):
    for y in range(2*n-1):
        if(y>x and y<2*n-x-2):
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()





